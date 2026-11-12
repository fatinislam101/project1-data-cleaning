import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)

month_counts = df["Order_Date"].dt.month.value_counts().sort_index()

print("Orders per month")
print(month_counts)

print("\nTotal Orders:", month_counts.sum())

month_counts.plot(kind="bar")

plt.title("Number of Orders per Month")
plt.xlabel("Month")
plt.ylabel("Number of Orders")

plt.tight_layout()
plt.show()
