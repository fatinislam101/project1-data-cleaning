import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"Data\cleaned_data.csv",
    parse_dates=["Order_Date"]
)
print(df.shape)
print(df["Order_Date"].dtype)
city_counts=df["City"].value_counts()
print(city_counts)

city_counts.plot(kind="bar")

plt.title("Number of orders per city")
plt.xlabel("City")
plt.ylabel("Number of orders")
plt.tight_layout()
plt.show()
