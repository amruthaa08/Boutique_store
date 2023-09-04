from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from secret_key import api_key

# openapi key setup
import os
os.environ["OPENAI_API_KEY"] = api_key

llm = OpenAI(temperature=0.7)

def generate_boutique_name_items(origin):
    # chain 1: boutique name
    prompt_template_name = PromptTemplate(
        input_variables=["origin"], 
        template="I want to open a dress boutique for {origin} dresses. Suggest a fancy name for this."
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="boutique_name")

    # chain 2: dress items
    prompt_template_items = PromptTemplate(
        input_variables=["boutique_name", "origin"],
        template="""Suggest some {origin} dress items for {boutique_name}.
                    Return it as comma separated values"""
    )

    items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="dress_items")

    chain = SequentialChain(
        chains = [name_chain, items_chain],
        input_variables = ["origin"],
        output_variables = ["boutique_name", "dress_items"]
    )

    response = chain({"origin": origin})

    return response

if __name__ == "__main__":
    print(generate_boutique_name_items("Italian"))
