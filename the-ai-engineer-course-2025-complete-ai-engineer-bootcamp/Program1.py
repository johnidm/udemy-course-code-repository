"""
streamlit run Program1.py
"""

import streamlit as st

from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma.vectorstores import Chroma
import os

from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.environ["OPENAI_API_KEY"]

chat = ChatOpenAI(model_name="gpt-4o", temperature=0, openai_api_key=openai_api_key)

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

vectorstore = Chroma(
    embedding_function=embedding, persist_directory="./intro-to-ai"
)

retriever = vectorstore.as_retriever(
    search_type="mmr", search_kwargs={"k": 5, "lambda_mult": 0.7}
)

PROMPT_RETRIEVING_S = """You will receive a question from a student taking the Intro to AI course.
Answer the question using only the provided context."""

PROMPT_TEMPLATE_RETRIEVING_H = """This is the question:
{question}

This is the context:
{context}"""

prompt_retrieving_s = SystemMessage(PROMPT_RETRIEVING_S)
prompt_template_retrieving_h = HumanMessagePromptTemplate.from_template(
    PROMPT_TEMPLATE_RETRIEVING_H
)

chat_prompt_template_retrieving = ChatPromptTemplate(
    [prompt_retrieving_s, prompt_template_retrieving_h]
)

str_output_parser = StrOutputParser()

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | chat_prompt_template_retrieving
    | chat
    | str_output_parser
)

st.header("Intro to AI Course Assistant", divider=True)

st.subheader("Question")

question = st.text_area("Enter your question here")

st.subheader("Answer")

if st.button("Ask"):
    if question:
        response_placeholder = st.empty()
        response_text = ""

        result = chain.stream(question)

        for chunk in result:
            response_text += chunk
            response_placeholder.markdown(response_text)
    else:
        st.warning("Please enter a question.", icon="⚠️")
