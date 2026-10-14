# サメ博士・宋青松のオンライン水族館 LP

テレビで話題の若手研究者・宋青松（サメ博士）のオンライン水族館 ランディングページ。
LINE公式アカウント登録への導線を主目的とした、深海テーマのモバイルファーストLP。

## 公開URL

| 用途 | URL |
|---|---|
| 本番（GitHub Pages） | https://matsumotohitomi.github.io/samehakase-lp/ |
| 正本リポジトリ（本リポ） | bluebearteam/samehakase-lp |
| プレビュー（Claude Artifact・非公開） | https://claude.ai/code/artifact/bd86fef6-260c-48d2-b530-a4bc667e2d0d |

## ディレクトリ構成

```
samehakase-lp/
├── index.html          … LP本体（1ページ）
├── css/style.css       … スタイル（モバイルファースト / @media 768px・1024px）
├── js/script.js        … 追従ヘッダー・追従CTA、ギャラリー自動スクロール、出現アニメ
├── images/             … 画像・SVGアイコン（ページが参照する素材一式）
├── build-artifact.py   … CSS/JS/画像をインライン化し単一HTML(artifact.html)を生成
├── README.md
└── HANDOFF.md          … 申し送り（未完了箇所・運用メモ）※必読
```

将来的に WordPress 化する想定で、HTML / CSS / JS を分割した構成にしてあります。

## ローカルでの確認

```bash
cd samehakase-lp
python3 -m http.server 8791
# ブラウザで http://localhost:8791/index.html
```

## 単一HTML（Artifact / 配布用）の生成

```bash
python3 build-artifact.py
# → artifact.html（CSS/JS/画像をbase64で内包した自己完結ファイル）
```

- Google Fonts のリンクのみ外部参照（Artifact の CSP で許可されているホスト）。
- 使用フォント: Zen Kaku Gothic New / Reggae One（大タイトル）/ Yomogi（手書き風バッジ）/ Montserrat。

## デプロイ（GitHub Pages）

`index.html` / `css` / `js` / `images` をコミットして push すれば GitHub Pages が自動反映（約20〜30秒）。

## 未完了・申し送り

**→ [HANDOFF.md](HANDOFF.md) を必ず参照してください。**
（動画エリアが仮置き、LINE/Instagram/剥製販売の実URL差し込みが未対応です）
