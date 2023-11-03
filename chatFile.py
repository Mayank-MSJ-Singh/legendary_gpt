from langchain import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
vectoreStore = ''
'''
agent = OpenAI(temperature = 1)
conv = RetrievalQAWithSourcesChain(llm=agent,retriever = vectoreStore.as_retriever(), memory=ConversationSummaryMemory())
'''
def chat_connection(chat, temp = 1):
    print("1")
    global vectoreStore, conv, agent
    print("2")
    return agent.predict(chat)
    print("3")
    print("4")
    print("5")

def web(url):
    global vectoreStore, conv, agent
    print("url - 1")
    loaders = UnstructuredURLLoader(urls=url)
    print("url - 2")
    data = loaders.load()
    print("url - 3")

    splitter = CharacterTextSplitter(separator='.',
                                     chunk_size=200,
                                     chunk_overlap=10)
    print("url - 4")
    docs = splitter.split_documents(data)
    print("url - 5")
    embedding = OpenAIEmbeddings()
    print("url - 6")
    vectoreStore = FAISS.from_documents(data, embedding)
    print("url - 7")
    agent = OpenAI(temperature=1)
    conv = RetrievalQAWithSourcesChain.from_llm(llm=agent, retriever=vectoreStore.as_retriever())

"""
def chatnew(chat, urls = "https://en.wikipedia.org/wiki/French_Revolution"):
    url = []
    url.append(urls)
    web(url)
    ans = chat_connection(chat)
    return ans
    print("hello")
"""