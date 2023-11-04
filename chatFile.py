from langchain import OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from PyPDF2 import PdfReader
url = []
vectoreStore= ''
"""owner_data = "Owner - Mayank"
embedding = OpenAIEmbeddings()
vectoreStore = FAISS.from_documents(owner_data, embedding)"""

'''
agent = OpenAI(temperature = 1)
conv = RetrievalQAWithSourcesChain(llm=agent,retriever = vectoreStore.as_retriever(), memory=ConversationSummaryMemory())
'''
def web(urls):
    global vectoreStore, conv, agent, url
    url = []
    url.append(urls)
    print("url - 1")
    loaders = UnstructuredURLLoader(urls=url)
    print("url - 2")
    data = loaders.load()
    print("url - 3")

    splitter = CharacterTextSplitter(separator='\n',
                                     chunk_size=200,
                                     chunk_overlap=20)
    print("url - 4")
    docs = splitter.split_documents(data)
    print("url - 5")
    embedding = OpenAIEmbeddings()
    print("url - 6")
    vectoreStore = FAISS.from_documents(docs, embedding)
    print("url - 7")

def read_pdf(pdfs):
    text = ''
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for pages in pdf_reader.pages:
            text += pages.extract_text()
    return text
def chat_connection(temperature = 1):
    print("1")
    global vectoreStore, conv, agent
    print("2")
    print("3")
    agent = OpenAI(temperature=temperature)
    print("4")
    conv = RetrievalQAWithSourcesChain.from_llm(llm=agent, retriever=vectoreStore.as_retriever())
    print("5")


def chatnew(chat):
    global conv
    response = conv({"question": chat}, return_only_outputs=True)
    answer = response['answer']
    return answer
"""
web("https://en.wikipedia.org/wiki/French_Revolution")
chat_connection()
print(chatnew("hi"))
"""