from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from LangChain.config import OPENAI_API_KEY

# ChatOpenAI クラスを使って LLM インスタンスを作成
llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,  # OpenAIのAPIキーを設定
    model="gpt-4o-mini",             # 使用するモデル名（gpt-4o-mini）
    max_tokens=100,                  # 生成される最大トークン数を100に制限
    temperature=0.7,                 # 応答のランダム性を設定（0.1でほぼ決定論的）
    top_p=0.95,                      # nucleus samplingのパラメータ（上位95%まで考慮）
    n=1,                             # 応答の生成数（1個）
    stop=None                        # 応答の停止トークン（なし）
)

# プロンプトテンプレート
template = "あなたは優秀なPythonの専門家です。次の質問に答えてください。{question}"
prompt = PromptTemplate(input_variables=["question"],template=template)
output_parser = StrOutputParser() # 応答を文字列として解析

chain = prompt | llm | output_parser
response = chain.invoke({"question": "Pythonとは何ですか？"})
print(response)


# # チャットプロンプトテンプレート
# chat_prompt = ChatPromptTemplate.from_messages([
#     ("system", "あなたは優秀なPythonの専門家です。"),
#     ("user", "{question}")
# ])
# prompt = template.invoke(
#     {
#         "question": "Pythonとは何ですか？"
#     }
# )
# response = llm.invoke(prompt)
# print(response)


