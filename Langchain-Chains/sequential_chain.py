from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser |prompt2 | model | parser

result = chain.invoke({'topic':'unemployment in India'})

print(result)

chain.get_graph().chain_ascii()