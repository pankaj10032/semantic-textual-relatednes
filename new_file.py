# ASP = 100  # Average Selling Price
# manufacturing_cost = 40  # Cost of Manufacturing
# marketing_spends = 20  # Marketing and Other Spends
# discount = 0.10  # 10% discount
# growth_rate = 0.10  # 10% growth rate
# retention_rate = 0.80  # 80% retention rate
# attracted_users = 0.50  # 50% of new users attracted with discount

# # Monthly Sales data from the previous year
# monthly_sales = [200000, 220000, 242000, 266200, 292820, 322102, 354312, 389743, 428718, 471590, 518748, 570623]

# # Fixed Costs
# initial_investment = 1000000
# monthly_rent = 50000

# # Calculate initial revenue and customer base
# initial_revenue = sum(monthly_sales) * ASP
# initial_customer_base = monthly_sales[-1]*110/100

# variable_cost_per_unit = manufacturing_cost + marketing_spends
# monthly_revenue_per_unit = ASP * (1 - discount)  # Revenue per unit sold

# cumulative_profit = -initial_investment  # Initialize cumulative profit
# months = 0  # Initialize months counter

# while cumulative_profit < 0:
#     # Calculate revenue and variable cost
#     revenue = monthly_revenue_per_unit * initial_customer_base
#     variable_cost = variable_cost_per_unit * initial_customer_base
#     # Calculate total cost (variable cost + fixed costs)
#     total_cost = variable_cost + monthly_rent
#     initial_customer_base *= (1 + growth_rate)  # Increase customer base with growth rate
#     initial_customer_base *= retention_rate  # Retain existing customers
#     initial_customer_base += attracted_users * initial_customer_base  # Attract new users with discount
#     # Calculate profit
#     profit = revenue - total_cost
#     cumulative_profit += profit
#     months += 1

# print("Months to become profitable:", months)


import math

# Constants
avg_selling_price = 100.00
cost_of_manufacturing = 40.00
marketing_spends = 20.00
extra_discount = 10  # in percentage
initial_investment = 1000000
monthly_rent = 50000
monthly_growth_rate = 0.10
existing_customer_retention_rate = 0.80
new_customer_attract_rate = 0.50
last_year_monthly_sales = 570623

# Calculating effective selling price after extra discount
effective_selling_price = avg_selling_price * (100 - extra_discount) / 100

# Initial number of existing customers
initial_existing_customers = 0.1 * last_year_monthly_sales

# Initial number of units sold
initial_units_sold = initial_existing_customers * existing_customer_retention_rate

# Monthly profit per unit sold
monthly_profit_per_unit = effective_selling_price - cost_of_manufacturing - marketing_spends

# Function to calculate monthly profit
def calculate_monthly_profit(existing_customers, new_customers):
    total_units_sold = existing_customers * existing_customer_retention_rate + new_customers * new_customer_attract_rate
    monthly_profit = total_units_sold * monthly_profit_per_unit - monthly_rent
    return monthly_profit

# Function to calculate cumulative profits until reaching profitability
def calculate_time_to_profitability():
    cumulative_profit = -initial_investment  # Start with initial investment as negative profit
    months = 0
    while cumulative_profit < 0:
        # Calculate number of existing and new customers for the current month
        existing_customers = initial_existing_customers * (1 + monthly_growth_rate) ** months
        new_customers = last_year_monthly_sales * (1 + monthly_growth_rate) ** months

        # Calculate monthly profit
        monthly_profit = calculate_monthly_profit(existing_customers, new_customers)

        # Accumulate monthly profit
        cumulative_profit += monthly_profit
        months += 1

    return months

# Calculate time to profitability
time_to_profitability = calculate_time_to_profitability()

print("Time to profitability in months:", time_to_profitability)
