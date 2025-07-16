from langchain_openai import OpenAI 
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
import argparse # used to create interfaces on the CLI



load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("--task", default="return a list of numbers 0 to 10")
parser.add_argument("--language", default="python")
args = parser.parse_args()



llm = OpenAI()

code_prompt = PromptTemplate(
    input_variables = ["language", "task"], # we must declare the input variables it needs to build the prompt
    template = "Write a very very short {language} function that will {task}"
)

test_prompt = PromptTemplate(
        input_variables=["language", "code"],
    template="Write a test for the following {language} code:\n{code}"
)

code_chain = code_prompt | llm
test_chain = test_prompt | llm


# Run the first chain to get the code
code_output = code_chain.invoke({
    "language": args.language,
    "task": args.task
})

# The generated text is usually under 'text'
generated_code = code_output

# Run the second chain to get the test, feeding the output
test_output = test_chain.invoke({
    "language": args.language,
    "code": generated_code
})

generated_test = test_output


print(">>>> Generated Code:")
print(generated_code)
print(">>>> Generated Test:")
print(generated_test)