from ibm_watsonx_orchestrate.agent_builder.tools import tool

@tool(name="monthly_payment_calc",
      description="Calculates the monthly repayment for a policy using the annual policy premium and interest rate.")
def monthly_payment_calc(premium:float, rate:float):
    n =  12  # total number of months
    r = rate / (100 * 12)  # interest per month
    monthly_payment = premium * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1))
    return monthly_payment



