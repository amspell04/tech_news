from langchain_ollama import ChatOllama

#lang smith?

def invoke_news_analysis(message: list[object]):
    agent = ChatOllama(
        model="gpt-oss:20b",
        temperature=0,
    )

    response = agent.invoke("Please review the following news articles/findings create a newspaper style" \
    " document covering the latest topics and events in tech. "
    )
    return response.content_blocks