import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)

print(df["Unit_Price"].describe().round(1))

df["Unit_Price"].hist(bins=10)


plt.title("Distribution of Unit Price")
plt.xlabel("Unit Price")
plt.ylabel("Frequency")

plt.show()