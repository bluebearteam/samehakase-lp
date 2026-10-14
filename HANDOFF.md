# 申し送り（HANDOFF） — サメ博士LP

最終更新: 2026-10-14

このファイルは、制作を引き継ぐ担当者向けの「未完了箇所」と「運用メモ」です。
サイト本体（index.html / css / js / images）は本番と同一の最新状態です。

---

## 🔴 未完了（先方からの素材待ち・要対応）

### 1. 動画（出演クリップ）エリアが仮置き
- 場所: `index.html` の **PROOF / MOVIE セクション**（`<section id="proof">` 内の `<div class="video-frame">`、145行目付近）
- 現状: 「動画・出演クリップ配置エリア」というプレースホルダー表示。
- 対応: 先方から **YouTube URL または 動画ファイル(mp4)** を受領後、ここに差し込む。
  - YouTube の場合: `<iframe>` 埋め込み（申請・許可は不要）。Cookie配慮で `youtube-nocookie.com`（プライバシー強化モード）推奨。
  - mp4 の場合: `<video>` タグで配置。
  - ⚠️ TV出演クリップは**放送局に著作権**あり。Web掲載の権利処理が済んでいるか先方に要確認。

### 2. プレースホルダーのリンク（`href="#"` のまま＝実URL未設定）
下記は `data-cta` 属性付きで仮リンク状態。実URLを差し込む。

| 箇所 | 行(目安) | data-cta | 差し込むURL |
|---|---|---|---|
| FV 緑のLINEボタン | 71 | line | LINE公式アカウント追加URL |
| FV Instagramカード | 119 | instagram | InstagramプロフィールURL |
| CUSTOM 剥製の購入ボタン | 297 | shop | カスタム剥製の販売ページURL |
| JOIN LINE登録ボタン | 356 | line | LINE公式アカウント追加URL |
| JOIN Instagramボタン | 368 | instagram | InstagramプロフィールURL |

- `data-cta="line"` は2箇所、`instagram` も2箇所あるので**まとめて同じURL**に。
- ヘッダーCTA・追従CTA・「#join」アンカーはページ内スクロール用なので変更不要。

---

## 🟡 運用メモ

### フォント
- 大タイトル「深海の世界へようこそ！」は**文字アウトラインSVG**（`images/title-outline.svg`）。文言を変える場合はSVGの作り直しが必要。
- 「＼サメっておもしろい／」バッジ＝**Yomogi（手書き風）**。別フォントにする場合は `index.html` のGoogle Fontsリンクと `build-artifact.py` 内のリンク文字列の**両方**を変更（下記参照）。

### build-artifact.py の注意
- Google Fontsのリンクは **`build-artifact.py` 内にハードコード**している（38〜41行目付近）。
  index.html 側でフォントを足しても、artifact.html に反映するには**こちらも手で合わせる**こと。

### FV（ヒーロー）PC表示の作り
- 背景 `images/hero-fv.jpg` を `cover`・`50% 8%` で配置。人物は画面幅に対し横 約68%・頭頂 約14% の位置。
- 「サメっておもしろい」バッジは**人物の頭上(約5px)に追従**するよう `top` を `vw` で計算（`css/style.css` の @media 768px 内）。画像を差し替える場合はこの係数の再調整が必要。
- SP（スマホ）表示は確定済みのため、PC側を触る際は **SPを壊さない**よう @media 内のみで調整する。

### 追従CTA（SP）
- `js/script.js` でヒーロー通過後に表示、JOINセクション表示時に非表示。
- 非表示時は影ごと画面外へ退避させ「頭だけ覗く」不具合を解消済み（`css/style.css` `.sticky-cta` の transform）。

---

## ✅ 対応済み（これまでの主な修正）

- 先方PPTXコメント（2026-09受領）の文言修正を全反映（PROOF/BENEFIT/FOR YOU/CUSTOM/PROFILE/JOIN 等）。
- FVの背景差し替え・乗算フィルター調整・大タイトルのSVG化。
- PROFILE写真まわりのレイアウト刷新、BENEFITアイコンのSVG化。
- FOR YOU に人物写真＋巨大サメのPiP配置。
- FV(PC)のタイトル/本文サイズ・中央寄せ調整、バッジの位置/サイズ/手書き風フォント化。
- 追従ヘッダーのサメアイコンを新SVGに差し替え。
- JOIN見出しを「最新情報をいちばん近くで」に変更。

---

## リンク・参照

- 本番: https://matsumotohitomi.github.io/samehakase-lp/
- プレビュー(Artifact/非公開): https://claude.ai/code/artifact/bd86fef6-260c-48d2-b530-a4bc667e2d0d
- 文言修正の元指示メモ（ローカル保管）: `修正指示メモ_2026-09-07.md`、元スライド `ウェブぺージ訂正提案スライド-9_7_26.pptx`
  ※ 先方の内部コメントを含むため本（公開）リポジトリには未収録。必要時は別途共有。
