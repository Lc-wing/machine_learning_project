---
name: ai-scientist
description: Deploy and run Sakana AI's The AI Scientist (github.com/SakanaAI/AI-Scientist), an end-to-end research agent that generates ideas, writes and runs PyTorch experiments, plots results, writes a LaTeX paper, and reviews it. Also covers its standalone LLM paper reviewer. Use when the user asks to run The AI Scientist / AI-Scientist / Sakana, automate a full research loop on a code template (nanoGPT, 2D diffusion, grokking, etc.), or get an automated review of a paper PDF. 全自动科研、自动实验、自动写论文、AI 审稿。
---

# The AI Scientist（Sakana AI）

The AI Scientist 不是 skill，而是一个独立的 Python 程序。本 skill 告诉 Agent 如何在合适的机器上部署和运行它。以下命令和参数取自上游 README 及 `launch_scientist.py`，对应上游 commit `1de1dbc1f4ee2c5f61e9c94348d55eb51d7fa2eb`。上游更新后，以其 README 为准。

## 硬性规则

1. **它会执行大模型写的代码**。上游明确警告可能装危险的包、访问网络、派生进程。必须在容器里运行（见"容器化"），并限制网络访问。不要在存有敏感凭据的机器上直接运行。
2. **许可证强制披露**。用它生成的论文、报告，必须在摘要或 Methods/Disclosure 章节显著声明内容由机器生成。上游推荐写法：
   > "This manuscript was autonomously generated using [The AI Scientist](https://github.com/SakanaAI/AI-Scientist)."

   许可证还禁止把它用于监控与身份推断、无标注的逼真人像/音视频合成、无人监督的医疗诊断、犯罪预测。用户的用途涉及这些时，拒绝执行并说明原因。课程作业如果不允许提交 AI 生成内容，要提醒用户。
3. **不要装进当前项目仓库**。克隆到仓库之外（例如 `~/AI-Scientist`），除非用户要求，否则不要提交它的代码和输出。
4. **控制花费**。`--num-ideas` 默认是 50，必须显式设小（建议从 1–2 开始）。上游 FAQ 给的参考是使用 Claude Sonnet 3.5 时每篇论文通常不到 15 美元。

## 第 1 步：运行前检查（任一项不满足就停下，告诉用户缺什么）

```bash
nvidia-smi                      # 必须有 NVIDIA GPU + CUDA；上游说明纯 CPU 跑模板"耗时不可行"
docker --version                # 容器化运行需要
which pdflatex                  # 写 LaTeX 论文需要 texlive-full
python3 --version               # 上游使用 Python 3.11
```

检查所选模型对应的 API Key 环境变量是否存在，**只检查是否已设置，不要打印值**：

| 模型来源 | 环境变量 |
|----------|----------|
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| DeepSeek | `DEEPSEEK_API_KEY` |
| OpenRouter | `OPENROUTER_API_KEY` |
| Google Gemini | `GEMINI_API_KEY` |
| Claude via Bedrock | `AWS_ACCESS_KEY_ID`、`AWS_SECRET_ACCESS_KEY`、`AWS_REGION_NAME`，并 `pip install anthropic[bedrock]` |
| Claude via Vertex AI | `CLOUD_ML_REGION`、`ANTHROPIC_VERTEX_PROJECT_ID`、`VERTEXAI_LOCATION`、`VERTEXAI_PROJECT`，并 `pip install google-cloud-aiplatform anthropic[vertex]` |
| 文献检索（可选） | `S2_API_KEY`（Semantic Scholar）；没有就改用 OpenAlex，见第 4 步 |

在 Cursor 云端 Agent 里缺 Key 时，让用户到 Cursor Dashboard → Cloud Agents → Secrets 添加，而不是把 Key 写进代码或仓库。

## 第 2 步：安装

```bash
git clone https://github.com/SakanaAI/AI-Scientist.git ~/AI-Scientist
cd ~/AI-Scientist
conda create -n ai_scientist python=3.11
conda activate ai_scientist
sudo apt-get install texlive-full   # 很慢，可能需要按住回车
pip install -r requirements.txt
```

## 第 3 步：准备模板并跑基线

模板位于 `templates/`。上游维护三个：`nanoGPT`（含 `nanoGPT_lite`）、`2d_diffusion`、`grokking`。另有社区模板：`seir`、`mobilenetV3`、`sketch_rnn`、`MACE`、`earthquake-prediction`、`tensorf`、`probes`（上游不维护）。

每台机器都必须先跑一次基线 `run_0`，因为它用来做同硬件的耗时对比：

```bash
# NanoGPT：先准备数据，再跑基线
python data/enwik8/prepare.py
python data/shakespeare_char/prepare.py
python data/text8/prepare.py
cd templates/nanoGPT && python experiment.py --out_dir run_0 && python plot.py

# 2D Diffusion
git clone https://github.com/gregversteeg/NPEET.git && (cd NPEET && pip install .) && pip install scikit-learn
cd templates/2d_diffusion && python experiment.py --out_dir run_0 && python plot.py

# Grokking
pip install einops
cd templates/grokking && python experiment.py --out_dir run_0 && python plot.py
```

## 第 4 步：运行论文生成

```bash
python launch_scientist.py --model "claude-3-5-sonnet-20241022" --experiment nanoGPT_lite --num-ideas 2
```

常用参数：

| 参数 | 作用 |
|------|------|
| `--model` | 必须是 `ai_scientist/llm.py` 中 `AVAILABLE_LLMS` 里的名字，例如 `claude-3-5-sonnet-20241022`、`gpt-4o-2024-05-13`、`gpt-4.1`、`o3-mini`、`deepseek-chat`、`deepseek-reasoner`、`gemini-2.0-flash` |
| `--experiment` | `templates/` 下的模板名，默认 `nanoGPT` |
| `--num-ideas` | 生成的想法数，**默认 50，务必改小** |
| `--parallel N` / `--gpus 0,1` | 多 GPU 并行跑多个想法 |
| `--engine openalex` | 没有 Semantic Scholar Key 时改用 OpenAlex（需 `pip install pyalex` 并设置 `OPENALEX_MAIL_ADDRESS`） |
| `--skip-idea-generation` / `--skip-novelty-check` | 复用已有想法，跳过生成或查新 |
| `--improvement` | 根据自动审稿意见再改进一轮论文 |

上游建议只用不弱于原版 GPT-4 的模型；审稿环节用 GPT-4o 效果最好，其他模型有偏正面或格式不合规的问题。

产出位于 `results/<experiment>/<时间戳>_<想法名>/`，包括实验代码与结果、`log.txt`、`<想法名>.pdf`、`review.txt`，以及用了 `--improvement` 时的 `<想法名>_improved.pdf`。没有生成 PDF 或审稿是常见情况，成功率取决于模板、模型和想法复杂度。

## 只用自动审稿

```python
import openai
from ai_scientist.perform_review import load_paper, perform_review

client = openai.OpenAI()
review = perform_review(
    load_paper("report.pdf"),
    "gpt-4o-2024-05-13",
    client,
    num_reflections=5,
    num_fs_examples=1,
    num_reviews_ensemble=5,
    temperature=0.1,
)
review["Overall"], review["Decision"], review["Weaknesses"]
```

## 容器化

上游提供了社区贡献的 `experimental/Dockerfile`：

```bash
docker run -e OPENAI_API_KEY=$OPENAI_API_KEY -v `pwd`/templates:/app/AI-Scientist/templates <AI_SCIENTIST_IMAGE> \
  --model gpt-4o-2024-05-13 --experiment 2d_diffusion --num-ideas 2
```

## 自定义模板

参照现有模板，新建 `templates/<名字>/`，包含：`experiment.py`（接收 `--out_dir`）、`plot.py`、`prompt.json`、`seed_ideas.json`、`latex/template.tex`。文件名和输出 JSON 格式要与现有模板一致。目前只支持能用代码表达的研究想法。

## 向用户汇报

说明用了哪个模型和模板、跑了几个想法、输出目录在哪、哪些想法成功产出了 PDF 和审稿分数。同时提醒用户：自动生成的论文必须人工核实实验、引用和结论，并按许可证要求披露。
