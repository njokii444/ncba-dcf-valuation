import numpy as np

# NCBA's financial data
fcf = 19_700_000_000  # 2023 Free Cash Flow in KES
growth_rate = 0.06  # 6% estimated growth rate
discount_rate = 0.14  # 14% WACC
years = 5  # Projection for 5 years
terminal_growth_rate = 0.03  # 3% terminal growth rate

# Debt and cash details
net_debt = 280_000_000_000  # Total debt minus cash
shares_outstanding = 1_650_000_000  # Total NCBA shares

# Project Free Cash Flows
fcf_projections = [fcf * (1 + growth_rate) ** i for i in range(1, years + 1)]

# Discounted Free Cash Flows
discounted_fcf = [fcf_projections[i] / (1 + discount_rate) ** (i + 1) for i in range(years)]

# Terminal Value using Perpetuity Growth Model
terminal_value = fcf_projections[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
discounted_terminal_value = terminal_value / (1 + discount_rate) ** years

# Enterprise Value (EV)
enterprise_value = sum(discounted_fcf) + discounted_terminal_value

# Equity Value (EV - Net Debt)
equity_value = enterprise_value - net_debt

# Price Per Share
price_per_share = equity_value / shares_outstanding

# Print results
print(f"Enterprise Value: {enterprise_value:,.2f} KES")
print(f"Equity Value: {equity_value:,.2f} KES")
print(f"Intrinsic Value Per Share: {price_per_share:,.2f} KES")


import numpy as np
import matplotlib.pyplot as plt

# NCBA's financial data (Refined)
fcf = 19_700_000_000  # 2023 Free Cash Flow in KES
growth_rate = 0.05  # 5% estimated growth rate
discount_rate = 0.15  # 15% WACC
years = 5  # Projection for 5 years
terminal_growth_rate = 0.025  # 2.5% terminal growth rate

# Debt and cash details (Updated)
net_debt = 280_000_000_000  # Updated Net Debt
shares_outstanding = 1_650_000_000  # Total NCBA shares

# Project Free Cash Flows
fcf_projections = [fcf * (1 + growth_rate) ** i for i in range(1, years + 1)]

# Discounted Free Cash Flows
discounted_fcf = [fcf_projections[i] / (1 + discount_rate) ** (i + 1) for i in range(years)]

# Terminal Value using Perpetuity Growth Model
terminal_value = fcf_projections[-1] * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
discounted_terminal_value = terminal_value / (1 + discount_rate) ** years

# Enterprise Value (EV)
enterprise_value = sum(discounted_fcf) + discounted_terminal_value

# Equity Value (EV - Net Debt)
equity_value = enterprise_value - net_debt

# Price Per Share
price_per_share = equity_value / shares_outstanding

# Print results
print(f"Enterprise Value: {enterprise_value:,.2f} KES")
print(f"Equity Value: {equity_value:,.2f} KES")
print(f"Intrinsic Value Per Share: {price_per_share:,.2f} KES")

# --- Plot the Free Cash Flow Projections ---
years_range = np.arange(1, years + 1)

plt.figure(figsize=(8, 5))
plt.plot(years_range, fcf_projections, marker='o', linestyle='-', label="Projected FCF")
plt.plot(years_range, discounted_fcf, marker='s', linestyle='--', label="Discounted FCF", color='red')

plt.axhline(y=discounted_terminal_value, color='green', linestyle=':', label="Discounted Terminal Value")

plt.xlabel("Years")
plt.ylabel("Free Cash Flow (KES)")
plt.title("Projected vs Discounted Free Cash Flows")
plt.legend()
plt.grid()
plt.show()
