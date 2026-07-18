from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_groq import ChatGroq
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()



model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

loader = TextLoader('cricket.txt',encoding='utf-8')

prompt = PromptTemplate(
    template='Give me a summary of the following poem - \n {poem}',
    input_variables=['poem']
)

parser = StrOutputParser()

docs = loader.load()

print(type(docs))


print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'poem':docs[0].page_content}))