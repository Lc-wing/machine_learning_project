#!/usr/bin/env python3
"""Rebuild the talk, scripts, source data, and figures. Never invokes git.

Run: MPLCONFIGDIR=/tmp/sketchthinker-mpl python3 docs/presentation/build_presentation.py
Dependencies: python-pptx, matplotlib, python-docx, Pillow; Poppler CLI tools.
Optional QA uses the repository skills. LibreOffice renders the finished deck.
"""
from pathlib import Path
import csv
import json
import os
import re
import subprocess
import sys
from datetime import timedelta

os.environ.setdefault('MPLCONFIGDIR', '/tmp/sketchthinker-mpl')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from PIL import Image
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from docx import Document
from docx.shared import Inches as DInches, Pt as DPt

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
FIG = HERE / 'figures'
OUT = HERE / 'output'
PDF = HERE / 'paper/2601.02825.pdf'
SKILLS = ROOT / '.agents/skills'
for folder in [FIG, OUT]:
    folder.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(SKILLS / 'nature-figure/scripts'))
from audit_panel_alignment import require_matplotlib_panel_alignment

NAVY = '#112B43'
TEAL = '#087F8C'
BLUE = '#456D99'
GRAY = '#81909D'
RED = '#B85341'
LIGHT = '#EEF4F6'
INK = '#203546'
WHITE = '#FFFFFF'
FONT = 'Liberation Sans'
AUTHORS = ['Ruiyang Zhang', 'Dongzhan Zhou', 'Zhedong Zheng']
W, H = 13.333333, 7.5
plt.rcParams.update({'font.family': FONT, 'font.size': 18,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.labelcolor': INK, 'text.color': INK, 'xtick.color': INK,
    'ytick.color': INK, 'axes.edgecolor': GRAY, 'pdf.fonttype': 42,
    'svg.fonttype': 'none', 'legend.frameon': False})

def run(args):
    return subprocess.run([str(a) for a in args], check=True, capture_output=True, text=True)

def words(text):
    return len(re.findall(r"\b[\w]+(?:[’'-][\w]+)*\b", text))

def clock(seconds):
    return f'{int(round(seconds))//60:02d}:{int(round(seconds))%60:02d}'

def extract():
    run(['pdftotext', '-layout', PDF, HERE/'paper/2601.02825.txt'])
    text = (HERE/'paper/2601.02825.txt').read_text()
    metadata = run(['pdfinfo', PDF]).stdout
    title = re.search(r'^Title:\s+(.+)$', metadata, re.M)[1]
    expected = 'SketchThinker-R1: Towards Efficient Sketch-Style Reasoning in Large Multimodal Models'
    assert title == expected
    assert 'Preprint' in text.split('\f')[0]
    pages = text.split('\f')
    for author in AUTHORS:
        assert author in pages[0], author
    assert re.search(r'0\.5\s*×\s*Raccuracy.*0\.4\s*×\s*Rformat.*0\.1\s*×\s*Rthinking-style', pages[3])
    judge_prompt = re.search(r'The template for building.*?\[THINKING\]', pages[3], re.S)[0]
    assert '[THINKING]' in judge_prompt and '[IMAGE]' not in judge_prompt and '[QUESTION]' not in judge_prompt
    page6 = pages[5]
    split = page6.index('Table 1:')
    blocks = [page6[:split], page6[split:]]
    names = ['Vanilla-R1','Constrained CoT','Chain-of-Draft','C3oT',
             'VeriThinker','L1','ThinkPrune']
    data = {}
    for scale, block in zip([7,3], blocks):
        rows = {}
        for name in names + [f'SketchThinker-R1-{scale}B']:
            match = re.search(r'^'+re.escape(name)+r'\s+(.+)$', block, re.M)
            assert match, (name, scale)
            vals = [float(v) for v in re.findall(r'\d+\.\d+', match[1])]
            assert len(vals) == 12, (name, vals)
            rows[name] = vals
        data[scale] = rows
    assert data[3]['Vanilla-R1'][3:5] == [26.9, 151.2]
    assert data[3]['SketchThinker-R1-3B'][3:5] == [25.3, 72.7]
    assert data[7]['Vanilla-R1'][3] == 31.0
    assert data[7]['SketchThinker-R1-7B'][3] == 31.7
    with (FIG/'paper-table-data.csv').open('w') as f:
        writer = csv.writer(f)
        writer.writerow(['table','scale_B','method','benchmark','accuracy_pct','reasoning_tokens','EoT'])
        for scale, rows in data.items():
            for name, vals in rows.items():
                for j,b in enumerate(['MMMU','MATH-Vision','VisuLogic','PhyX']):
                    writer.writerow([1 if scale==7 else 2,scale,name,b,*vals[j*3:j*3+3]])
    # Exact row checks tie all additional plotted/displayed paper numbers to pdftotext.
    checks = {
      'p7_stage_cold': (6, r'61\.4\s+114\.5\s+0\.536'),
      'p7_stage_rl': (6, r'62\.1\s+152\.2\s+0\.408'),
      'p7_stage_both': (6, r'62\.8\s+64\.3\s+0\.977'),
      'p7_judge_no_sft': (6, r'61\.0\s+72\.1\s+0\.846'),
      'p16_dynamic': (15, r'Dynamic Weight\s+63\.2\s+62\.5\s+1\.011'),
      'p16_staged': (15, r'Staged Weight\s+63\.0\s+63\.8\s+0\.987'),
      'p17_data_5k': (16, r'5K\s+66\.1\s+56\.8\s+1\.164'),
      'p18_interpretability': (17, r'Vanilla-R1-7B\s+3\.95\s+SketchThinker-R1-7B\s+4\.25'),
      'p20_training_hours': (19, r'Vanilla-R1-7B\s+2\.70h\s+SketchThinker-R1-7B\s+2\.21h'),
    }
    for key,(page,pattern) in checks.items():
        assert re.search(pattern,pages[page]), key
    (OUT/'number-verification.json').write_text(json.dumps({
        'title':title,'authors':AUTHORS,'venue':'ICLR 2026 (poster); OpenReview ZSMDuKtYbt; arXiv:2601.02825 v1 used as extraction source, text and numbers identical to the proceedings version',
        'reward_weights':{'accuracy':0.5,'format':0.4,'thinking_style':0.1},
        'judge_input':'Thinking text only; neither image nor question (Section 2.2 prompt)',
        'math_vision_3b':{'accuracy_pct':[26.9,25.3],'reasoning_tokens':[151.2,72.7]},
        'math_vision_7b':{'accuracy_pct':[31.0,31.7]},
        'table_rows_verified':64,'additional_exact_row_checks':list(checks),
        'source':'paper/2601.02825.txt, generated with pdftotext -layout',
        'main_batch_size':128,'appendix_batch_size':512,
        'policy':'Paper values are extracted/checked; derived arithmetic and proposed design values are labeled separately.'
    }, indent=2)+'\n')
    # Native PDF image extraction for Figure 1; only page 2 is extracted.
    run(['pdfimages','-f','2','-l','2','-j',PDF,FIG/'paper-fig1'])
    # Figure 2 is a mixture of vector and raster content: render and crop the complete panel.
    # PDF coordinates are top-left origin, in points; no data or text altered.
    crops=[('paper-fig2-pipeline',3,(106,82,505,170)),
           ('paper-fig3-left-case',8,(108,80,304,402)),
           ('paper-fig3-circles',8,(165,82,250,146))]
    manifest=[]
    for name,page,(x0,y0,x1,y1) in crops:
        dpi=240; k=dpi/72
        run(['pdftoppm','-f',page,'-l',page,'-r',dpi,'-x',round(x0*k),
             '-y',round(y0*k),'-W',round((x1-x0)*k),'-H',round((y1-y0)*k),
             '-singlefile','-png',PDF,FIG/name])
        manifest.append({'file':name+'.png','page':page,'crop_pt':[x0,y0,x1,y1],
                         'method':'pdftoppm 240 dpi crop','slide':3 if page==3 else (2 if 'circles' in name else 'source asset only')})
    (OUT/'asset_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return title, data

def export(fig,name):
    fig.canvas.draw()
    require_matplotlib_panel_alignment(fig,json_out=str(FIG/f'{name}.alignment.json'),
        tolerance_pt=1.5,gutter_tolerance_pt=1.5,strict=True)
    for ext in ['png','pdf','svg']:
        fig.savefig(FIG/f'{name}.{ext}',dpi=220,facecolor='white')
    plt.close(fig)

def charts(data):
    v=data[7]['Vanilla-R1']; s=data[7]['SketchThinker-R1-7B']
    benchmarks=['MMMU','MATH-Vision','VisuLogic','PhyX']
    # Claim: the 7B comparison substantially lowers tokens in every listed domain.
    fig,ax=plt.subplots(figsize=(8.4,4.7));fig.subplots_adjust(left=.23,right=.96,top=.9,bottom=.16)
    yy=list(range(4)); ax.barh([y-.18 for y in yy],v[1::3],.32,color=GRAY,label='Vanilla-R1')
    ax.barh([y+.18 for y in yy],s[1::3],.32,color=TEAL,label='SketchThinker-R1-7B')
    ax.set_yticks(yy,benchmarks);ax.invert_yaxis();ax.set_xlim(0,270)
    ax.set_xlabel('Average reasoning tokens')
    ax.legend(loc='lower center',bbox_to_anchor=(.5,1.02),ncol=2,fontsize=14)
    for y,b,a in zip(yy,v[1::3],s[1::3]):
        ax.text(b+4,y-.18,f'{b:.1f}',va='center',fontsize=16)
        ax.text(a+4,y+.18,f'{a:.1f}',va='center',fontsize=16,color=TEAL)
    export(fig,'tokens-7b')
    # Claim: MMMU reported operating point is favorable on both measured axes.
    fig,ax=plt.subplots(figsize=(9.3,4.8));fig.subplots_adjust(left=.12,right=.98,top=.93,bottom=.19)
    offsets={'Vanilla-R1':(-8,14),'Constrained CoT':(-10,-26),'Chain-of-Draft':(-5,20),
       'C3oT':(18,-20),'VeriThinker':(-5,14),'L1':(8,18),'ThinkPrune':(-5,-30),
       'SketchThinker-R1-7B':(10,5)}
    for name,vals in data[7].items():
        hero=name.startswith('Sketch'); x,y=vals[:2][::-1]
        ax.scatter(x,y,s=150 if hero else 75,color=TEAL if hero else GRAY,zorder=3)
        ax.annotate(name,(x,y),xytext=offsets[name],textcoords='offset points',fontsize=16,
                    color=TEAL if hero else INK)
    ax.set(xlim=(48,218),ylim=(57.7,63.7),xlabel='Average reasoning tokens  ← fewer',ylabel='Answer accuracy (%)')
    ax.grid(axis='y',alpha=.15);export(fig,'accuracy-vs-tokens-mmmu')
    # Claim: combined stages reach a stronger operating point than either alone.
    fig,ax=plt.subplots(figsize=(8.5,4.7));fig.subplots_adjust(left=.15,right=.98,top=.92,bottom=.18)
    for name,x,y,off in [('Cold start only',114.5,61.4,(-80,-40)),
                         ('RL only',152.2,62.1,(-55,16)),('Cold start + RL',64.3,62.8,(10,-5))]:
        ax.scatter(x,y,s=180,color=TEAL if '+' in name else GRAY,zorder=3)
        ax.annotate(f'{name}\n{y:.1f}% / {x:.1f} tokens',(x,y),xytext=off,
                    textcoords='offset points',fontsize=17)
    ax.set(xlim=(48,187),ylim=(60.9,63.4),xlabel='Average reasoning tokens',ylabel='MMMU accuracy (%)')
    ax.grid(axis='y',alpha=.15);export(fig,'stages-ablation')
    # Claim: the 3B accuracy comparison is task-dependent; include every benchmark.
    v3=data[3]['Vanilla-R1'];s3=data[3]['SketchThinker-R1-3B']
    delta=[s3[i]-v3[i] for i in [0,3,6,9]]
    fig,ax=plt.subplots(figsize=(8.7,4.8));fig.subplots_adjust(left=.16,right=.97,top=.93,bottom=.2)
    ax.bar(benchmarks,delta,color=[TEAL if d>=0 else RED for d in delta],width=.5)
    ax.axhline(0,color=GRAY,lw=1);ax.set_ylim(-2.1,1.6)
    ax.set_ylabel('Accuracy change (percentage points)')
    for x,d in enumerate(delta):ax.text(x,d+(.1 if d>=0 else -.15),f'{d:+.1f}',ha='center',va='bottom' if d>=0 else 'top',fontsize=20)
    export(fig,'accuracy-delta-3b')
    # Standalone clean pipeline, also reproduced with editable PPTX shapes.
    fig,ax=plt.subplots(figsize=(12,3.7));ax.set(xlim=(0,12),ylim=(0,3.7));ax.axis('off')
    items=[('Sketch-Mode\nCold Start','Long traces → GPT-5 sketches\nSupervised multimodal policy'),
           ('SketchJudge\nReward Model','Long = 0; sketch = 1\nText-only style classifier'),
           ('Sketch-Thinking\nReinforcement Learning','GRPO on new questions\nAccuracy + format + style')]
    for i,(head,body) in enumerate(items):
        x=.2+i*4
        ax.add_patch(FancyBboxPatch((x,.5),3.55,2.6,boxstyle='round,pad=0.05',facecolor=LIGHT,edgecolor='none'))
        ax.text(x+.18,2.65,head,fontsize=20,fontweight='bold',va='top')
        ax.text(x+.18,1.45,body,fontsize=16,va='top',linespacing=1.6)
        if i<2:ax.add_patch(FancyArrowPatch((x+3.6,1.8),(x+3.94,1.8),arrowstyle='-|>',mutation_scale=20,color=TEAL))
    export(fig,'pipeline-redraw')

def rgb(color):return RGBColor.from_string(color.lstrip('#'))
def box(slide,x,y,w,h,color=LIGHT,outline=None,rounded=False):
    sh=slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE,
        Inches(x),Inches(y),Inches(w),Inches(h))
    sh.fill.solid();sh.fill.fore_color.rgb=rgb(color)
    if outline:sh.line.color.rgb=rgb(outline)
    else:sh.line.fill.background()
    return sh
def text(slide,txt,x,y,w,h,size=22,color=INK,bold=False,align=None):
    sh=slide.shapes.add_textbox(Inches(x),Inches(y),Inches(w),Inches(h))
    tf=sh.text_frame;tf.word_wrap=True
    tf.margin_left=tf.margin_right=Inches(.02);tf.margin_top=tf.margin_bottom=Inches(.015)
    for i,line in enumerate(txt.split('\n')):
        p=tf.paragraphs[0] if i==0 else tf.add_paragraph();p.text=line
        p.font.name=FONT;p.font.size=Pt(size);p.font.bold=bold;p.font.color.rgb=rgb(color)
        p.space_after=Pt(8)
        if align is not None:p.alignment=align
    return sh
def pic(slide,name,x,y,w,h):
    path=FIG/name
    iw,ih=Image.open(path).size; k=min(w/iw,h/ih)
    return slide.shapes.add_picture(str(path),Inches(x+(w-iw*k)/2),Inches(y+(h-ih*k)/2),
                                    width=Inches(iw*k),height=Inches(ih*k))
def arrow(slide,x1,y1,x2,y2):
    sh=slide.shapes.add_shape(MSO_SHAPE.CHEVRON, Inches(x1), Inches(y1), Inches(x2-x1), Inches(y2-y1))
    sh.fill.solid();sh.fill.fore_color.rgb=rgb(TEAL);sh.line.fill.background();return sh
def table(slide,headers,rows,x,y,width,height,widths=None,font=18):
    sh=slide.shapes.add_table(len(rows)+1,len(headers),Inches(x),Inches(y),Inches(width),Inches(height))
    t=sh.table
    if widths:
        for col,wi in zip(t.columns,widths):col.width=Inches(wi)
    for r,vals in enumerate([headers]+rows):
        for c,val in enumerate(vals):
            cell=t.cell(r,c);cell.text=str(val);cell.margin_left=Inches(.12);cell.margin_right=Inches(.08)
            cell.margin_top=Inches(.06);cell.margin_bottom=Inches(.04);cell.vertical_anchor=MSO_ANCHOR.MIDDLE
            cell.fill.solid();cell.fill.fore_color.rgb=rgb(NAVY if r==0 else (LIGHT if r%2 else WHITE))
            for p in cell.text_frame.paragraphs:
                p.font.name=FONT;p.font.size=Pt(font);p.font.color.rgb=rgb(WHITE if r==0 else INK);p.font.bold=(r==0)
    return sh

def slides(title,data,content):
    prs=Presentation();prs.slide_width=Inches(W);prs.slide_height=Inches(H)
    prs.core_properties.title=title
    prs.core_properties.subject='15-minute paper analysis and research plan pitch'
    prs.core_properties.author='Presentation group — editable member table on slide 1'
    elapsed=0
    for idx,c in enumerate(content):
        n=idx+1;s=prs.slides.add_slide(prs.slide_layouts[6]);dark=n in [1,13,16]
        s.background.fill.solid();s.background.fill.fore_color.rgb=rgb(NAVY if dark else WHITE)
        fg=WHITE if dark else INK
        box(s,0,0,.16,H,TEAL)
        text(s,'PART I  /  PAPER ANALYSIS' if c['part']=='I' else 'PART II  /  RESEARCH PLAN',.48,.2,11,.3,11,TEAL if not dark else '#82D5D5',True)
        if n!=1:text(s,c['title'],.5,.72,12.2,.9,30,fg,True)
        text(s,f'{n:02d} / 16',12.0,7.06,.8,.25,10,fg)
        text(s,c['source'],.5,7.05,11.2,.29,10,'#BDCED9' if dark else '#607889')
        if n==1:
            text(s,title,.55,.8,12.0,1.6,32,WHITE,True)
            text(s,' · '.join(AUTHORS),.55,2.57,12,.4,21,WHITE)
            text(s,'University of Macau · Shanghai AI Laboratory',.55,3.06,12,.4,19,'#BDCED9')
            text(s,'ICLR 2026',.55,3.6,12,.4,22,'#82D5D5',True)
            text(s,'EDIT — Group members & contributions',.55,4.25,12,.35,16,WHITE)
            table(s,['Name','Contribution','%'],[[f'[Name {a}]','[contribution]','[xx%]'] for a in 'ABCD'],
                  .55,4.75,8.2,1.85,[2.1,4.6,1.5],16)
            text(s,'12 min\nPaper analysis\n\n3 min\nResearch pitch',9.35,4.7,3.1,1.95,19,WHITE)
        elif n==2:
            text(s,'Image + question',.7,1.85,3.3,.4,24,bold=True)
            pic(s,'paper-fig3-circles.png',.9,2.5,2.8,2.5)
            text(s,'Three externally tangent circles\nFind the area between centers',.65,5.2,3.5,1.0,18)
            arrow(s,4.25,3.2,4.7,3.65)
            text(s,'Verbose explanation',5.05,1.85,3.4,.4,22,bold=True)
            for k,ww in enumerate([5.2,4.8,5.6,4.4,5.0]):box(s,5.1,2.6+k*.35,ww,.08,'#C7D3DC')
            text(s,'Textual sketch',5.05,4.65,6.8,.45,24,TEAL,True)
            text(s,'Tangency → distances → triangle → area',5.05,5.28,7.3,.7,22)
            text(s,'Goal: retain the key logical flow',5.05,6.2,7.3,.4,20,TEAL,True)
        elif n==3:
            heads=['1 · Cold Start','2 · SketchJudge','3 · Sketch RL']
            bodies=['GPT-5 rewrites long traces\nSupervise the answering model',
                    'Train long / sketch labels\nScore thinking text only',
                    'GRPO on new questions\nAccuracy + format + style']
            for j,(head,body) in enumerate(zip(heads,bodies)):
                x=.55+4.2*j;box(s,x,1.95,3.82,2.25,LIGHT)
                text(s,head,x+.16,2.12,3.5,.5,24,TEAL,True)
                text(s,body,x+.16,2.9,3.5,1.12,18)
                if j<2:arrow(s,x+3.91,2.8,x+4.13,3.14)
            pic(s,'paper-fig2-pipeline.png',.8,4.6,11.8,1.95)
            text(s,'Top: redrawn pipeline · Bottom: original Figure 2',.6,6.63,11,.3,16)
        elif n==4:
            table(s,['Existing long-trace source','Sampled questions'],[['LLaVA-CoT-100K','10,000'],['Vision-R1-cold','10,000']],.65,1.95,6.7,1.9,[4.9,1.8],20)
            text(s,'20K',8.2,2.0,4.0,.9,54,TEAL,True)
            text(s,'SketchColdStart-20K',8.2,3.0,4.2,.5,22,bold=True)
            text(s,'Long trace  →  GPT-5 rewrite  →  numbered sketch',.75,4.45,12,.6,26,TEAL,True)
            text(s,'Supervised next-token training',.75,5.35,11,.5,24,bold=True)
            text(s,'Qwen2.5-VL-7B-Instruct · also evaluated at 3B',.75,6.0,11.5,.45,20)
        elif n==5:
            text(s,'Original long trace',.8,2.0,5,.5,25,bold=True)
            text(s,'Rewritten sketch',.8,3.15,5,.5,25,TEAL,True)
            text(s,'Label 0',5.1,2.0,2,.5,25)
            text(s,'Label 1',5.1,3.15,2,.5,25,TEAL)
            box(s,8.0,1.9,4.45,2.55,LIGHT)
            text(s,'Qwen2.5-7B-Instruct',8.2,2.2,4.0,.5,22,TEAL,True)
            text(s,'40K labeled thinking traces\nBinary style judgment',8.2,3.0,4.0,1.15,20)
            box(s,.75,5.0,11.8,1.2,LIGHT)
            text(s,'Judge input: thinking text only',.95,5.10,11,.45,27,TEAL,True)
            text(s,'Sees neither the image nor the question',.95,5.72,11,.35,19)
            text(s,'Style label ≠ verified visual support',.95,6.34,11,.4,23,RED,True)
        elif n==6:
            text(s,'R = 0.5 accuracy + 0.4 format + 0.1 thinking-style',.65,1.98,12.1,.7,29,TEAL,True)
            table(s,['Illustrative response','Accuracy','Format','Style','Reward'],
                  [['Correct, valid format, sketch','1','1','1','1.0'],['Wrong, valid format, sketch','0','1','1','0.5']],
                  .7,3.0,11.9,1.8,[6.0,1.4,1.4,1.4,1.7],18)
            text(s,'Five rollouts → relative advantages → clipped policy update',.8,5.25,11.7,.6,25,bold=True)
            text(s,'KL penalty anchors the policy · no default token penalty',.8,6.15,11.7,.4,21)
        elif n==7:
            table(s,['Evaluation domain','Benchmark'],[['Broad reasoning','MMMU'],['Visual mathematics','MATH-Vision'],['Visual logic','VisuLogic'],['Visual physics','PhyX']],.65,1.9,6.3,3.6,[3.5,2.8],21)
            text(s,'Report separately',7.65,1.95,4.8,.5,25,TEAL,True)
            text(s,'Answer accuracy (%)\nAverage reasoning tokens',7.65,2.7,4.8,1.5,24)
            text(s,'EoT = accuracy / tokens',7.65,4.65,4.8,.5,22,bold=True)
            text(s,'RL training: 250 questions × 4 sources = SketchRL-1K',.75,6.05,12,.5,22)
        elif n==8:
            pic(s,'tokens-7b.png',.4,1.75,8.5,4.85)
            v=data[7]['Vanilla-R1'];a=data[7]['SketchThinker-R1-7B']
            table(s,['Accuracy (%)','Vanilla','Sketch'],[[b,f'{v[j*3]:.1f}',f'{a[j*3]:.1f}'] for j,b in enumerate(['MMMU','MATH-Vision','VisuLogic','PhyX'])],
                  9.0,2.1,3.85,3.5,[1.85,1.0,1.0],16)
            text(s,'64.7–76.5% fewer tokens',8.95,5.95,3.95,.72,22,TEAL,True)
        elif n==9:
            pic(s,'accuracy-vs-tokens-mmmu.png',.55,1.7,12.1,4.95)
            text(s,'Reported operating points · uncertainty not reported',.75,6.6,11.6,.3,18)
        elif n==10:
            pic(s,'stages-ablation.png',.35,1.78,8.9,4.95)
            text(s,'Judge fine tuning',9.3,2.0,3.5,.65,24,TEAL,True)
            text(s,'With SFT\n62.8% / 64.3 tokens\n\nWithout SFT\n61.0% / 72.1 tokens',9.3,2.95,3.5,2.65,21)
            text(s,'MMMU · 7B backbone',9.3,6.15,3.4,.4,18)
        elif n==11:
            pic(s,'accuracy-delta-3b.png',.55,1.75,9.0,4.95)
            v=data[3]['Vanilla-R1'];a=data[3]['SketchThinker-R1-3B']
            text(s,'MATH-Vision',9.7,2.2,3.0,.5,23,RED,True)
            text(s,f'{v[3]:.1f}% → {a[3]:.1f}%',9.7,3.0,3.0,.6,25,RED,True)
            text(s,'Reasoning tokens',9.7,3.85,3.0,.4,20,bold=True)
            text(s,f'{v[4]:.1f} → {a[4]:.1f}',9.7,4.4,3.0,.5,25,TEAL,True)
            text(s,'Token savings do not\nguarantee accuracy gains',9.7,5.35,3.0,1.2,20)
        elif n==12:
            table(s,['MMMU reward schedule','Accuracy (%)','Tokens'],[['Fixed','62.8','64.3'],['Staged','63.0','63.8'],['Dynamic','63.2','62.5']],.65,1.95,7.1,2.65,[3.9,1.8,1.4],20)
            text(s,'More RL data',8.35,1.98,4.0,.5,24,TEAL,True)
            text(s,'1K → 5K samples\n62.8% → 66.1% MMMU',8.35,2.75,4.0,1.1,22)
            text(s,'Training time',.75,5.1,5.5,.45,24,TEAL,True)
            text(s,'2.70 h → 2.21 h · 8 H800 GPUs',.75,5.8,6.9,.55,23)
            text(s,'Human readability study',8.35,4.85,4.0,.5,22,TEAL,True)
            text(s,'20 jointly correct examples\n5 evaluators',8.35,5.55,4.0,1.0,21)
        elif n==13:
            text(s,'What the paper establishes',.75,1.95,11.8,.5,25,'#82D5D5',True)
            text(s,'Large token savings in the tested 7B comparisons',.75,2.75,11.7,.7,29,WHITE)
            for j,(h,b) in enumerate([('Grounding','Text-only style judge'),('Uncertainty','Point estimates; small human audit'),('Reproduction','Rollout batch size: 128 vs 512')]):
                y=3.85+j*.82;text(s,h,.8,y,2.6,.4,21,'#82D5D5',True);text(s,b,3.7,y,8.5,.5,22,WHITE)
            text(s,'Open question: what evidence survives compression?',.75,6.5,12,.4,25,WHITE,True)
        elif n==14:
            text(s,'Preserving Visual Evidence in\nCompressed Multimodal Reasoning',.7,1.72,11.8,1.0,27,TEAL,True)
            # Editable triangle and example: explicit design illustration, not a paper result.
            for x1,y1,x2,y2 in [(1.0,5.4,2.5,3.4),(2.5,3.4,4.0,5.4),(1.0,5.4,4.0,5.4)]:
                ln=s.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,Inches(x1),Inches(y1),Inches(x2),Inches(y2));ln.line.color.rgb=rgb(TEAL);ln.line.width=Pt(2)
            text(s,'40°',1.38,4.83,1,.4,22);text(s,'60°',3.08,4.83,1,.4,22);text(s,'x',2.3,3.82,.5,.4,24)
            text(s,'Image-only angle readings',.9,5.85,3.8,.5,18)
            text(s,'Sufficient sketch',5.0,3.25,7.0,.45,24,TEAL,True)
            text(s,'Angles read: 40° and 60°\nTriangle sum: x = 180° − 40° − 60° = 80°',5.0,4.02,7.4,1.3,24)
            text(s,'Explicit premises + valid deductions\nAccept alternative complete proofs',5.0,5.72,7.2,.95,21)
        elif n==15:
            table(s,['Shared cold start + rewritten data','Auxiliary reward'],[['Evidence arm','Image + question + trace'],['Style arm','Thinking text only'],['Zero-component arm','No auxiliary component']],.65,1.9,12.0,2.55,[7.2,4.8],21)
            text(s,'2,400 rendered problems · checked image pairs',.75,4.8,11.8,.5,25,TEAL,True)
            text(s,'Match achieved tokens within 5% · include judge compute',.75,5.55,11.8,.5,24,bold=True)
            text(s,'Measure: accuracy · premise retention · human sufficiency · paired correctness',.75,6.3,11.8,.6,20)
        elif n==16:
            stages=[('M1','Reproduce\nCompute pilot'),('M2','Annotate\nChecked pairs'),('M3','Calibrate\nJudge gate'),('M4','Train\nThree seeds'),('M5','Controls\nFrozen tests'),('M6','Human audit\nRelease')]
            for j,(mo,lab) in enumerate(stages):
                x=.65+j*2.1;box(s,x,1.95,1.88,.5,TEAL)
                text(s,mo,x,2.03,1.88,.3,18,WHITE,True,PP_ALIGN.CENTER)
                text(s,lab,x,2.72,1.93,1.25,18,WHITE)
            text(s,'Judge gate: false acceptance ≤10% · sufficient recall ≥70%',.75,4.45,11.8,.5,24,'#82D5D5',True)
            text(s,'Success: higher retention and accuracy at matched resources',.75,5.38,11.8,.55,25,WHITE)
            text(s,'Null results and failure cases are deliverables',.75,6.25,11.8,.45,25,WHITE,True)
        count=words(c['script']);assert count==c['target'],(n,count,c['target'])
        duration=count/130*60
        c['words']=count;c['start']=clock(elapsed);c['end']=clock(elapsed+duration)
        c['seconds']=duration
        s.notes_slide.notes_text_frame.text=c['script']
        elapsed+=duration
    assert sum(c['words'] for c in content[:13])==1560
    assert sum(c['words'] for c in content[13:])==390
    prs.save(HERE/'sketchthinker-presentation.pptx')
    return prs

def scripts(content):
    intro='English speaker script · 16 slides · 1,950 spoken words · 15:00 at 130 words per minute. Part I: 1,560 words / 12:00. Part II: 390 words / 3:00. Timing excludes unscripted discussion. Word counts exclude headings, source cues, and metadata; hyphenated words count as one.'
    md=['# SketchThinker-R1 — Speaker script','',intro,'']
    doc=Document();sec=doc.sections[0];sec.header.paragraphs[0].text='SketchThinker-R1 | Presentation script'
    sec.top_margin=sec.bottom_margin=DInches(.7)
    style=doc.styles['Normal'];style.font.name=FONT;style.font.size=DPt(11)
    doc.add_heading('SketchThinker-R1 — Speaker script',0);doc.add_paragraph(intro)
    for i,c in enumerate(content,1):
        heading=f"Slide {i:02d} — {c['title']}"
        meta=f"Part {c['part']} · {c['start']}–{c['end']} · {c['words']} words · {c['seconds']:.1f} seconds"
        md += ['## '+heading,'',meta,'',c['script'],'','*Source cue (not spoken): '+c['source']+'*','']
        if i>1:doc.add_page_break()
        doc.add_heading(heading,1);doc.add_paragraph(meta,'Subtitle');doc.add_paragraph(c['script']);doc.add_paragraph('Source cue (not spoken): '+c['source'])
    md+=['## Word counts per slide','','| Slide | Part | Words | Time window |','|---|---|---:|---|']
    doc.add_page_break();doc.add_heading('Word counts per slide',1)
    t=doc.add_table(rows=1,cols=4);t.style='Light Shading Accent 1'
    for cell,val in zip(t.rows[0].cells,['Slide','Part','Words','Time window']):cell.text=val
    for i,c in enumerate(content,1):
        vals=[str(i),c['part'],str(c['words']),f"{c['start']}–{c['end']}"]
        md.append('| '+' | '.join(vals)+' |')
        for cell,val in zip(t.add_row().cells,vals):cell.text=val
    md+=['| **Part I** | | **1,560** | **12:00** |','| **Part II** | | **390** | **3:00** |','| **Total** | | **1,950** | **15:00** |','']
    doc.add_paragraph('Part I: 1,560 words / 12:00. Part II: 390 words / 3:00. Total: 1,950 words / 15:00.')
    (HERE/'speaker-script.md').write_text('\n'.join(md))
    doc.save(HERE/'speaker-script.docx')
    (OUT/'timing-and-words.json').write_text(json.dumps([{k:c[k] for k in ['title','part','words','start','end','seconds']} for c in content],indent=2)+'\n')

def verify(prs,content):
    reopened=Presentation(HERE/'sketchthinker-presentation.pptx')
    assert len(reopened.slides)==16
    assert abs(reopened.slide_width/reopened.slide_height-16/9)<1e-5
    for i,s in enumerate(reopened.slides):
        assert content[i]['script'] == s.notes_slide.notes_text_frame.text
        for sh in s.shapes:
            assert sh.left>=0 and sh.top>=0
            assert sh.left+sh.width<=reopened.slide_width+2,(i+1,'right')
            assert sh.top+sh.height<=reopened.slide_height+2,(i+1,'bottom')
            if sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    # Footer / section metadata explicitly use 10–11 pt; body floor is 16 pt.
                    if .65*914400 < sh.top < 7*914400:
                        assert p.font.size is None or p.font.size.pt>=16,(i+1,p.text)
    bad=re.compile(r'\b(perhaps|might|arguably|somewhat|seem(?:s|ingly)?|maybe|possibly|probably)\b',re.I)
    assert not bad.search(' '.join(c['script'] for c in content))
    print(json.dumps({'slides':16,'paper_words':1560,'plan_words':390,'total_words':1950,
                      'duration':'15:00','notes_match':True,'bounds_pass':True}))

def main():
    content=json.loads((HERE/'talk-content.json').read_text())
    title,data=extract();charts(data);prs=slides(title,data,content);scripts(content);verify(prs,content)

if __name__=='__main__':main()
