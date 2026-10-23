# Reference field audit

Checked 2026-10-22 against the linked primary arXiv landing pages using web access. Each title, listed author sequence, initial preprint year, and arXiv identifier matches the source. This is primary-record verification, not independent bibliographic cross-corroboration. No journal volume, issue, or page range is claimed; all entries consistently cite preprints. DeepSeek-R1 and Qwen2.5-VL deliberately abbreviate long author lists with “et al.”; other lists are complete. MathVista and Let's Verify Step by Step use 2023 preprint years rather than later venue years. No uncertain reference remains requiring an UNVERIFIED comment.

Correction (2026-10-22): SketchThinker-R1 is not arXiv-only; it was published at ICLR 2026 as a poster, and the bibliography entry now cites the ICLR version with the arXiv ID kept as a secondary link. A text comparison of the proceedings PDF with arXiv v1 found identical body text, tables and pagination (28 pages); the only differences are the running header and an added acknowledgment. Every number the proposal and talk use (reward weights 0.5/0.4/0.1, Tables 1–2) is unchanged.

| Key | Primary record | Preprint year | Checked authors | Status |
|---|---|---|---|---|
| wei | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models.](https://arxiv.org/abs/2201.11903) | 2022 | Jason Wei; Xuezhi Wang; Dale Schuurmans; Maarten Bosma; Brian Ichter; Fei Xia; Ed Chi; Quoc Le; Denny Zhou | Fields match |
| deepseek | [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning.](https://arxiv.org/abs/2501.12948) | 2025 | DeepSeek-AI; Daya Guo; Dejian Yang; Haowei Zhang; et al. | Fields match |
| sketch | [SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models.](https://arxiv.org/abs/2601.02825) | 2026 | Ruiyang Zhang; Dongzhan Zhou; Zhedong Zheng | Fields match; published at ICLR 2026 (poster), [OpenReview](https://openreview.net/forum?id=ZSMDuKtYbt), [proceedings PDF](https://proceedings.iclr.cc/paper_files/paper/2026/file/a1f0c0cd6caaa4863af5f12608edf63e-Paper-Conference.pdf) |
| sot | [Sketch-of-Thought: Efficient LLM Reasoning with Adaptive Cognitive-Inspired Sketching.](https://arxiv.org/abs/2503.05179) | 2025 | Simon A. Aytes; Jinheon Baek; Sung Ju Hwang | Fields match |
| sone | [s1: Simple test-time scaling.](https://arxiv.org/abs/2501.19393) | 2025 | Niklas Muennighoff; Zitong Yang; Weijia Shi; Xiang Lisa Li; Li Fei-Fei; Hannaneh Hajishirzi; Luke Zettlemoyer; Percy Liang; Emmanuel Candès; Tatsunori Hashimoto | Fields match |
| lightman | [Let's Verify Step by Step.](https://arxiv.org/abs/2305.20050) | 2023 | Hunter Lightman; Vineet Kosaraju; Yura Burda; Harri Edwards; Bowen Baker; Teddy Lee; Jan Leike; John Schulman; Ilya Sutskever; Karl Cobbe | Fields match |
| turpin | [Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting.](https://arxiv.org/abs/2305.04388) | 2023 | Miles Turpin; Julian Michael; Ethan Perez; Samuel R. Bowman | Fields match |
| mathverse | [MathVerse: Does Your Multi-modal LLM Truly See the Diagrams in Visual Math Problems?](https://arxiv.org/abs/2403.14624) | 2024 | Renrui Zhang; Dongzhi Jiang; Yichi Zhang; Haokun Lin; Ziyu Guo; Pengshuo Qiu; Aojun Zhou; Pan Lu; Kai-Wei Chang; Peng Gao; Hongsheng Li | Fields match |
| mathvista | [MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts.](https://arxiv.org/abs/2310.02255) | 2023 | Pan Lu; Hritik Bansal; Tony Xia; Jiacheng Liu; Chunyuan Li; Hannaneh Hajishirzi; Hao Cheng; Kai-Wei Chang; Michel Galley; Jianfeng Gao | Fields match |
| mathvision | [Measuring Multimodal Mathematical Reasoning with MATH-Vision Dataset.](https://arxiv.org/abs/2402.14804) | 2024 | Ke Wang; Junting Pan; Weikang Shi; Zimu Lu; Mingjie Zhan; Hongsheng Li | Fields match |
| qwen | [Qwen2.5-VL Technical Report.](https://arxiv.org/abs/2502.13923) | 2025 | Shuai Bai; Keqin Chen; Xuejing Liu; Jialin Wang; et al. | Fields match |
| grpo | [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models.](https://arxiv.org/abs/2402.03300) | 2024 | Zhihong Shao; Peiyi Wang; Qihao Zhu; Runxin Xu; Junxiao Song; Xiao Bi; Haowei Zhang; Mingchuan Zhang; Y.K. Li; Y. Wu; Daya Guo | Fields match |

## Claims requiring full-text checks

- [SketchThinker-R1 §2.2](https://arxiv.org/html/2601.02825v1#S2.SS2): judge prompt contains thinking text only; no question or image.
- [§2.3, Eq. 5](https://arxiv.org/html/2601.02825v1#S2.SS3): 0.5 accuracy + 0.4 format + 0.1 style.
- [Table 2](https://arxiv.org/html/2601.02825v1#S3): MathVision 26.9 vs 25.3 at 3B, explicitly reported without generalizing.
- Source §3 reports GPT-5 rewriting. The proposal treats effects as a hypothesis and audits content in length-preserving controls.
- [MathVerse official repository](https://github.com/ZrrSkywalker/MathVerse): testmini and its evaluation route confirmed. Public versions are grouped with original items in uncertainty estimation.

All 12 bibliography keys are cited in the text; no cited key lacks an entry.
