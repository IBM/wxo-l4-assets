import string

from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool(name="life_quote",
      description="Calculates a coverage premium for life insurance when provided with amount of cover required and the age of the customer.")
def life_quote(amount:int, age:int):

    # the baseline cost for cover is 0.1% of the cover amount
    base_cost = amount * 0.001
    age_factor = (age / 1.5) * 0.1
    age_supplement = base_cost * age_factor

    quote = base_cost + age_supplement
    return quote
