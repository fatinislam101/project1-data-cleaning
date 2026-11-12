
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)
summary=df.groupby("Product_Category")["Profit"].agg(["mean","std","count"]).round(1)

print(summary)
df.boxplot(column="Profit",by="Product_Category")

plt.suptitle("")
plt.title("Profit Distribution by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()