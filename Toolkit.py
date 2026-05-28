from langchain_core.tools import tool
@tool
def calcuate_interest(principal:float,rate:float,time:int):
    """Use this tool for ANY question involving loans,interest,mortages or total repay amount.
    Inputs:principal(amount borrowed),rate(yearly percentage),time(years)."""
    amount=principal*((1+rate/100)**time)
    return f"The total amount after {time} years will be: {amount:.2f}"