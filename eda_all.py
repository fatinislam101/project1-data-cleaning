import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset once
df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)

print("Dataset shape:", df.shape)

# Chart 1: Orders per City
city_orders = df["City"].value_counts()

city_orders.plot(kind="bar")
plt.title("Number of Orders per City")
plt.xlabel("City")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig(r"D:\DS-ML\Project1-data-cleaning\charts\city_orders.png")
plt.close()

# Chart 2: Missing Values per Column
missing_values = df.isna().sum().sort_values(ascending=False)

missing_values.plot(kind="barh")
plt.title("Missing Values per Column")
plt.xlabel("Number of Missing Values")
plt.ylabel("Column")
plt.tight_layout()
plt.savefig(r"D:\DS-ML\Project1-data-cleaning\charts\missing_values.png")
plt.close()

# Chart 3: Unit Price Distribution
df["Unit_Price"].plot(kind="hist", bins=10)
plt.title("Distribution of Unit Price")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(r"D:\DS-ML\Project1-data-cleaning\charts\unit_price_hist.png")
plt.close()

# Chart 4: Average Profit per Product Category
avg_profit = df.groupby("Product_Category")["Profit"].mean().sort_values(ascending=False)

avg_profit.plot(kind="bar")
plt.title("Average Profit per Product Category")
plt.xlabel("Product Category")
plt.ylabel("Average Profit")
plt.tight_layout()
plt.savefig(r"D:\DS-ML\Project1-data-cleaning\charts\avg_profit_category.png")
plt.close()

print("Charts saved")
