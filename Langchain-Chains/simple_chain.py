from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

template = PromptTemplate(
    template='Give me 5 facts about the {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = template |model | parser

result = chain.invoke({'topic':'cricket'})

print(result)

chain.get_graph().chain_ascii()