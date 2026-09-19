"""Estimate an electricity bill using a selected tariff."""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_choice = input("Which tariff? 11 or 31: ")
daily_use = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if tariff_choice == "11":
    price_per_kwh = TARIFF_11
else:
    price_per_kwh = TARIFF_31

estimated_bill = price_per_kwh * daily_use * billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
