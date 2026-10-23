"""Build the illustrative GIFs and promotional cards. Maintainer-only: pip install Pillow."""
from pathlib import Path
import json, os, re
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)

def font(size, bold=False):
    override = os.environ.get('PREFLIGHT_FONT')
    candidates = [override] if override else []
    candidates += [f'C:/Windows/Fonts/{"msyhbd" if bold else "msyh"}.ttc',
                   '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc']
    for path in candidates:
        if path and Path(path).is_file():
            return ImageFont.truetype(path, size)
    raise RuntimeError('Set PREFLIGHT_FONT to a CJK-capable font file for Chinese assets.')

def wrapped(draw, text, xy, face, width, fill, spacing=10):
    x,y=xy
    for paragraph in text.split('\n'):
        line=''
        for token in re.findall(r"[A-Za-z0-9][A-Za-z0-9'./-]*|\s+|.", paragraph):
            if draw.textlength(line+token, font=face) > width and line:
                draw.text((x,y), line.rstrip(), font=face, fill=fill)
                y += face.size + spacing
                line=token.lstrip()
            else:
                line += token
        if line:
            draw.text((x,y), line, font=face, fill=fill)
        y += face.size + spacing
    return y

durations=[4500,6500,4500,4500,5000,5000]
scenes={
 'en': [
  ('A new task', 'USER', 'Build a CSV import feature with required-column validation and ordinary tests.', 'A bounded task. Start with a direction.'),
  ('A short recommendation', 'PREFLIGHT', 'Routine · GPT-6.1 Sol / Medium / Standard, if available.\nWhy: clear scope and familiar validation.\nEscalate if conflicting requirements emerge.', 'Choose settings, then continue. Or keep current settings.'),
  ('You choose', 'MANUAL ACTION', 'Select your preferred model and effort in the client. The skill does not control the model picker.', 'A suggestion, with the choice in your hands.'),
  ('One word is enough', 'USER', 'Continue.', 'Accept execution. No assertion that a switch was verified.'),
  ('Back to work', 'EXPECTED BEHAVIOR', 'Proceed with the original implementation and its required checks, without another model-selection question.', 'One selection step for this task.'),
  ('Small follow-up', 'USER', 'Rename this one heading.\n\nExpected: make the small edit, without a fresh preflight.', 'Model choice, before the work starts.')
 ],
 'zh': [
  ('一个独立大任务', '用户', '做一个CSV导入功能，包含必填列校验和常规测试。', '边界明确的任务，先给一个起步方向。'),
  ('三行选型建议', 'PREFLIGHT', '常规 · GPT-6.1 Sol / Medium / Standard（如可用）\n理由：范围明确，主要是实现与校验。\n升级条件：出现冲突需求时再评估。', '选择后回复“继续”，也可按当前设置继续。'),
  ('由你选择', '手动操作', '你在客户端选择模型和推理档位。\n技能不会控制选择器或替你切换。', '建议清楚，选择仍在你手里。'),
  ('回复即可继续', '用户', '继续。', '接受执行，不声称已经验证模型切换。'),
  ('回到原任务', '预期行为', '继续原来的实现和必要检查，\n不再重复询问本轮模型配置。', '这个任务只做一次选择。'),
  ('普通追问保持安静', '用户', '把这一个标题改一下。\n\n预期：直接处理小改，不重新分档。', '大任务开工前，给你一句有依据的建议。')
 ]}
for lang, items in scenes.items():
    frames=[]
    for index,(title,role,body,foot) in enumerate(items):
        im=Image.new('RGB',(1080,700),'#F3F3ED')
        d=ImageDraw.Draw(im)
        d.text((52,30),'CODEX MODEL PREFLIGHT',font=font(22,True),fill='#1B3930')
        label='Illustrative workflow · not a live recording' if lang=='en' else '文字流程示意 · 非Codex真实录屏'
        d.text((52,65),label,font=font(18),fill='#63716B')
        d.text((52,114),title,font=font(39,True),fill='#17251F')
        d.rounded_rectangle((52,191,1028,526),radius=20,fill='white')
        d.text((80,216),role,font=font(18,True),fill='#36634F')
        end=wrapped(d,body,(80,261),font(26),922,'#1B2923',14)
        if end>515:
            raise RuntimeError(f'Overflow in {lang} frame {index+1}: {end}')
        wrapped(d,foot,(52,554),font(22),976,'#345745',10)
        for n in range(6):
            d.rounded_rectangle((52+n*165,647,202+n*165,653),radius=3,fill='#36795D' if n<=index else '#D5DDD5')
        d.text((967,603),f'{index+1} / 6',font=font(18),fill='#63716B')
        frames.append(im)
    frames[0].save(OUT/f'demo-{lang}.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=False,disposal=2)
    frames[1].save(OUT/f'demo-{lang}-poster.png')

cards={
 'en': ('Before you run.', 'One brief model recommendation for a substantial Codex task.', ['One starting point','One selection step','Public rules + cases'], 'A small, instruction-only skill. No automatic switching or savings promise.'),
 'zh': ('大任务，先选档。','开工前，给你一句有依据的模型与推理档位建议。',['给一个起步方向','大任务暂停一次','规则与案例公开'],'简约指令技能 · 用户手动选择模型 · 不承诺固定省额度比例')
}
for lang,(title,sub,cells,foot) in cards.items():
    im=Image.new('RGB',(1200,630),'#F3F3ED');d=ImageDraw.Draw(im)
    d.text((64,42),'CODEX MODEL PREFLIGHT',font=font(24,True),fill='#28674E')
    d.text((64,121),title,font=font(66,True),fill='#17251F')
    wrapped(d,sub,(66,225),font(28),1068,'#3C5145',12)
    for n,txt in enumerate(cells):
        x=64+n*364
        d.rounded_rectangle((x,340,x+344,442),radius=16,fill='white')
        wrapped(d,txt,(x+20,374),font(23,True),304,'#254B39',8)
    wrapped(d,foot,(64,499),font(22),1070,'#52645A',10)
    d.text((64,576),'v0.1.0  ·  MIT  ·  English / 简体中文',font=font(18),fill='#63716B')
    im.save(OUT/f'social-card-{lang}.png')

(OUT/'demo-scenes.json').write_text(json.dumps({'durations_ms':durations,'scenes':scenes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Built two 30-second GIFs, two poster frames, and two social cards.')
