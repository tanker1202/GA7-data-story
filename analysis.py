import pandas as pd
import matplotlib.pyplot as plt

# Quarterly CAC data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "CAC": [225.62, 231.07, 230.50, 234.72]
}

industry_target = 150

# Create DataFrame
df = pd.DataFrame(data)

# Calculate average
average_cac = df["CAC"].mean()
print(f"Average CAC = {average_cac:.2f}")  # Should match 230.48

# Plot CAC vs industry target
plt.figure(figsize=(8,5))
plt.plot(df["Quarter"], df["CAC"], marker='o', label="Company CAC")
plt.axhline(y=industry_target, color="r", linestyle="--", label="Industry Target (150)")
plt.title("Customer Acquisition Cost (2024)")
plt.xlabel("Quarter")
plt.ylabel("CAC ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("cac_trend.png")
plt.show()
