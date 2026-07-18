from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    temperature=0
)

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model2 = ChatHuggingFace(llm=llm)

class feedback(BaseModel):
    sentiment : Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='classify the sentiment of the following feedback into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write an appropriate response to the positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to the negative feedback \n {feedback}',
    input_variables=['feedback']
)

parser = StrOutputParser()

branch_chain = RunnableBranch(
    (lambda x:x.sentiment=='positive', prompt2 | model1 | parser),
    (lambda x:x.sentiment=='negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x:'could not find sentiment')
)

classifier_chain = prompt1 | model1 | parser2

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback':'This is a good phone'})

print(result)

chain.get_graph().print_ascii()