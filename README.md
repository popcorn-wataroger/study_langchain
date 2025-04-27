# 🤖 AIエージェントチャットアプリ
このアプリは、Streamlit上で動作するチャット型AIアシスタントです。  
チャット、Web検索、ドキュメント検索など複数機能を持ち、様々な質問に応答できます。

---

## 🚀 機能一覧

| 機能 | 説明 |
| --- | --- |
| 通常チャット | OpenAI APIを使った自然な会話が可能です。 |
| ウェブ検索 | 「天気」「調べて」などのキーワードに反応し、SerpAPIでインターネット検索を行います。 |
| 資料検索（Retrieval） | PDFなどの社内ドキュメントから情報を検索し、回答します（オプション機能）。 |
| LangGraphエージェント | LangGraphを使って複雑な思考・行動フローを制御するマルチエージェント機能です。 |

---

## 🛠 セットアップ手順

1. リポジトリをクローンまたはコードをダウンロードします。
2. 必要なPythonパッケージをインストールします。

```bash
pip install -r requirements.txt
```
3.  `config.py` ファイルを作成し、以下のように設定します。

```python
# config.py
OPENAI_API_KEY = "あなたのOpenAI APIキー"
SERP_API_KEY = "あなたのSerpAPIキー"

```

4. Streamlitアプリを起動します。

```bash
streamlit run stream_UI.py

```

---

## 📁 ディレクトリ構成

```
プロジェクト/
├── streamUI.py       # Streamlitアプリ本体（単体動作）
├── config.py         # APIキーなどの設定ファイル
├── Agent/
│   └── AI_agent.py    # 外部検索エージェントロジック
├── Retrieval/
│   └── RAG.py         # 社内資料検索（RAG）
├── Model/
│   └── gpt.py         # 通常チャット用モデル設定

```

---

## 📚 使用技術・ライブラリ

- **Streamlit** — チャットUI
- **LangChain** — チェーン構築とモデル管理
- **LangGraph** — マルチエージェント構成・柔軟なフロー制御
- **OpenAI API** — LLM（gpt-4o-mini）ベース応答
- **SerpAPI** — インターネット検索
- **Chroma（オプション）** — ドキュメント検索データベース

---

## ⚠ 注意事項

- **APIキー（OpenAI, SerpAPI）は絶対に公開リポジトリにコミットしないでください！**
- `config.py`は必ず`.gitignore`に登録することを推奨します。
