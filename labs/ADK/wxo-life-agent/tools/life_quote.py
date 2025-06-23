import string

from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool(name="life_quote",
      description="Calculates a coverage premium for life insurance when provided with amount of cover required, the age of the customer, and their involvement in extreme sports.")
def life_quote(amount:int, age:int, ex_sports:bool):

    # the baseline cost for cover is 0.1% of the cover amount
    base_cost = amount * 0.001
    age_factor = (age / 1.5) * 0.1
    age_supplement = base_cost * age_factor
    sport_factor = 0.35 if ex_sports else 0
    sport_supplement = age_supplement * sport_factor

    quote = base_cost + age_supplement + sport_supplement
    return quote
