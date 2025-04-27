# 🤖 AIエージェントチャットアプリ
このアプリは、**Streamlit**ベースで動作するシンプルなチャットインターフェースです。
以下の機能を備えたAIアシスタントを提供します：
- 通常の会話（ChatGPTベース）
- インターネット検索（SerpAPIを使用）
- 社内資料（PDF等）に基づく検索（※オプション）

---

## 🚀 機能一覧

| 機能 | 説明 |
| --- | --- |
| 通常チャット | OpenAI APIを使って質問応答ができます。 |
| ウェブ検索 | 質問に「天気」「検索」「調べて」などが含まれるとSerpAPI経由でインターネット検索を実施します。 |
| 資料検索（オプション） | （Retrievalフォルダにて実装）PDFなどの社内ドキュメントから情報検索できる機能を追加予定。 |

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
streamlit run streamUI.py

```

---

## 📁 ディレクトリ構成

```
プロジェクト/
├── streamUI.py       # Streamlitアプリ本体
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
- **OpenAI API** — LLM（gpt-4o-mini）ベース応答
- **SerpAPI** — インターネット検索
- **Chroma（オプション）** — ドキュメント検索データベース

---

## ⚠ 注意事項

- **APIキー（OpenAI, SerpAPI）は絶対に公開リポジトリにコミットしないでください！**
- `config.py`は必ず`.gitignore`に登録することを推奨します。
