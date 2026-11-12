import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)

avg_profit=df.groupby("Product_Category")["Profit"].mean().round(1)
print(avg_profit)

avg_profit=avg_profit.sort_values(ascending=False)

print(avg_profit)

avg_profit.plot(kind="bar")
plt.title("Average Profit by Product Category")
plt.xlabel("Product_Category")
plt.ylabel("Average Profit")

plt.tight_layout()
plt.show()