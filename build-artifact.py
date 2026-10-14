#!/usr/bin/env python3
"""index.html + css + js + 画像 を1ファイルの自己完結版 artifact.html にビルドする。
   - CSS/JS をインライン
   - 参照画像を data URI 化
   - 先頭に <meta charset="utf-8">（無いとローカル配信で文字化け）
   - Google Fonts のリンクは残す（Artifact の CSP で許可）
"""
import base64, re, pathlib

root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text(encoding='utf-8')
css  = (root / 'css/style.css').read_text(encoding='utf-8')
js   = (root / 'js/script.js').read_text(encoding='utf-8')

def data_uri(path):
    p = root / path
    ext = p.suffix.lower().lstrip('.')
    mime = {'jpg': 'image/jpeg', 'jpeg': 'image/jpeg',
            'png': 'image/png', 'webp': 'image/webp',
            'svg': 'image/svg+xml'}[ext]
    return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()

# OGP画像は自己完結アーティファクトでは不要（重い元PNGを埋め込まない）
html = html.replace('content="images/sousan_FV.png"', 'content=""')

# --- CSS内の画像参照 url("../images/xxx") をすべて data URI 化 ---
for m in sorted(set(re.findall(r'\.\./images/([^"\')]+)', css))):
    css = css.replace(f'../images/{m}', data_uri(f'images/{m}'))

# --- HTML内の画像参照 src="images/xxx" をすべて data URI 化 ---
for m in sorted(set(re.findall(r'images/([^"\')]+)', html))):
    html = html.replace(f'images/{m}', data_uri(f'images/{m}'))

body = re.search(r'<body[^>]*>(.*)</body>', html, re.S).group(1)
body = body.replace('<script src="js/script.js"></script>', '')

title = 'サメ博士のオンライン水族館'
fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Zen+Kaku+Gothic+New:wght@400;500;700;900'
         '&family=Reggae+One&family=Yomogi&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">')

out = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
{fonts}
<style>
{css}
</style>
{body}
<script>
{js}
</script>
'''

dest = root / 'artifact.html'
dest.write_text(out, encoding='utf-8')
print('built', dest, round(dest.stat().st_size / 1024 / 1024, 2), 'MB')
