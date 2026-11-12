import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)


missing=df.isna().sum()
print(missing)

missing_percent=(df.isna().sum()/len(df)*100).round(1)
print(missing_percent)

missing=missing.sort_values(ascending=False)

missing.plot(kind="barh")

plt.title("Missing values by column")
plt.xlabel("Number of missing values")
plt.ylabel("Columns")

plt.show()