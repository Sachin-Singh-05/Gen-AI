from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import TextLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_groq import ChatGroq
import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# os.environ["USER_AGENT"] = "MyLangChainApp/1.0"

load_dotenv()



model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

loader = TextLoader('cricket.txt',encoding='utf-8')

prompt = PromptTemplate(
    template='Answer the following questions \n {question}- from the following text \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url ="https://www.learnpytorch.io/pytorch_cheatsheet/"

loader = WebBaseLoader(url)

docs =loader.load()

chain = prompt | model | parser

result = chain.invoke({'question':'what is the topic we are learning ','text':docs[0].page_content})

print(result)