# streamUI.py

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from serpapi import GoogleSearch
import os
from config import OPENAI_API_KEY, SERP_API_KEY


# モデル設定（通常チャット用）
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model_name="gpt-4o-mini",
    max_tokens=300,
    temperature=0.3,
    top_p=0.9,
    n=1,
    stop=None
)
output_parser = StrOutputParser()

# プロンプトテンプレート
simple_prompt = PromptTemplate(
    input_variables=["question"],
    template="あなたは優秀なPythonアシスタントです。次の質問に答えてください：{question}"
)

simple_chain = simple_prompt | llm | output_parser

# SerpAPI検索
def search_web(query):
    params = {
        "q": query,
        "hl": "ja",
        "gl": "jp",
        "api_key": SERP_API_KEY
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    organic_results = result.get("organic_results", [])
    if not organic_results:
        return "検索結果が見つかりませんでした。"
    top_results = [f"{r['title']}: {r['snippet']}" for r in organic_results[:3]]
    return "\n\n".join(top_results)

# Streamlit設定
st.set_page_config(page_title="AIチャットアシスタント", page_icon="🤖", layout="wide")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 AIアシスタントチャット")

user_input = st.chat_input(placeholder="ここにメッセージを入力...")

# 過去のメッセージ表示
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        if "天気" in user_input or "検索" in user_input or "調べて" in user_input:
            st.markdown("🔎 ウェブ検索中...")
            result = search_web(user_input)
            st.markdown(result)
            st.session_state.messages.append({"role": "assistant", "content": result})
        else:
            response = simple_chain.invoke({"question": user_input})
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
