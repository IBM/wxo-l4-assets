import random
from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool(name="interest_rate_lookup",
      description="This tool will determine the interest rate to be used when calculating monthly payments for policies. The rate will be based on the annual premium of the policy.")
def rate_lookup(premium:float):
    rate = 15

    rate = random.randint(50, 100)
    rate = rate / 10
    return rate


