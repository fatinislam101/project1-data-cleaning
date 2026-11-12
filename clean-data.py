import pandas as pd
import numpy as np
df = pd.read_csv("Data/raw_data.csv")
# print(df.shape)
# print(df.dtypes)
# print(df.head())
# print(df.isna().sum())
# print(df.duplicated().sum())
# df["City"]=df["City"].str.strip().str.title()
# print(df["City"].unique())

# city_mapping={
#     "Hyd":"Hyderabad",
#     "Hyderbad":"Hyderabad",
#     "Bangalore":"Bengaluru"
    
# }
# df["City"]=df["City"].replace(city_mapping)
# print(df["City"].unique())
# print(df["Order_Date"].isna().sum())
# print(df["Order_Date"].dtypes)
# print(df["Order_Date"].isna().sum())
# print(df["Order_Date"].dropna().sample(15,random_state=1))
# df["Order_Date"]=pd.to_datetime(df["Order_Date"],format="mixed",dayfirst=True,errors="coerce")
# print(df["Order_Date"].isna().sum())
# print(df["Order_Date"])
# print(df["Order_Date"].min())
# print(df["Order_Date"].max())
# complete = df.dropna(subset=["Units_Sold", "Unit_Price", "Discount_%", "Sales_Amount"])

# print(len(complete))

# expected = complete["Units_Sold"] * complete["Unit_Price"] * (1 - complete["Discount_%"] / 100)

# diff = (complete["Sales_Amount"] - expected).abs().round(2)

# print(diff.describe())

# complete=df.dropna(subset=["Units_Sold","Unit_Price","Sales_Amount"])
# print(len(complete))
# expected=complete["Units_Sold"]*complete["Unit_Price"]
# diff=(complete["Sales_Amount"]-expected).abs().round(2)
# print(diff.describe())

# ratio=complete["Sales_Amount"]/expected
# print(ratio.describe())
# print(round(complete["Sales_Amount"].corr(expected),2))

# print(len(ratio))
# print(ratio.isna().sum())
# print(complete["Sales_Amount"].describe())
# print(expected.describe())

# print((expected == 0).sum())
# print(((expected == 0) & (complete["Sales_Amount"] == 0)).sum())
# print((complete["Sales_Amount"] == 0).sum())
# print((complete["Units_Sold"] < 0).sum())
# print((complete["Unit_Price"] < 0).sum())
# print((complete["Sales_Amount"] < 0).sum())

# normal = complete[
#     (complete["Units_Sold"] > 0) &
#     (complete["Unit_Price"] > 0) &
#     (complete["Sales_Amount"] > 0)
# ]

# print(len(normal))

# ratio = normal["Sales_Amount"] / ( normal["Units_Sold"] * normal["Unit_Price"])

# print(ratio.describe())

# has_disc=normal.dropna(subset=["Discount_%"])
# print(len(has_disc))
# ratio=has_disc["Sales_Amount"]/(has_disc["Units_Sold"]*has_disc["Unit_Price"])
# factor=1-has_disc["Discount_%"]/100
# gap=(ratio-factor).abs().round(2)
# print(gap.describe())

# print(df["Segment"].value_counts(dropna=False))
# print(df["Units_Sold"].describe())
# print(df["Unit_Price"].describe())

# print(df["Units_Sold"].value_counts(dropna=False).sort_index())
# df["Units_Clean"]=df["Units_Sold"].where(df["Units_Sold"]>0)
# print(df["Units_Clean"].isna().sum())
# print(df["Units_Sold"].isna().sum())


# df["Segment_Clean"] = df["Segment"].fillna("Unknown")
# df["Discount_missing"] = df["Discount_%"].isna()

# print(df["Segment_Clean"].value_counts())
# print(df["Discount_missing"].sum())

# df["Price_missing"]=df["Unit_Price"].isna()
# print(df["Price_missing"].sum())
# print(round(df["Price_missing"].mean()*100,1))

# print(df["Customer_Name"].nunique())
# print(df["Customer_Name"].str.strip().str.title().nunique())
# print(df["Product_Category"].nunique())
# print(df["Product_Category"].str.strip().str.title().nunique())
# print(df["Product_Name"].nunique())
# print(df["Product_Name"].str.strip().str.title().nunique())

# print(df["Product_Category"].value_counts())

# print((df["Sales_Amount"] == 0).sum())
# print((df["Sales_Amount"] < 0).sum())
# print((df["Profit"] < 0).sum())
# print(df["Profit"].describe())

# print(round(df["Sales_Amount"].corr(df["Profit"]),2))
# print(round(df["Units_Sold"].corr(df["Profit"]),2))

# cols=["Customer_Name","Product_Category","Product_Name","Units_Sold","Unit_Price","Discount_%","Sales_Amount"
#       ,"Order_Date","City","Segment","Profit"]
# print(df.duplicated(subset=cols).sum())

# import os

# os.makedirs("data", exist_ok=True)
# df.to_csv("data/cleaned_data.csv", index=False)

# check = pd.read_csv("data/cleaned_data.csv")
# print(check.shape)
# print(check["Order_Date"].dtype)

# check2=pd.read_csv("data/cleaned_data.csv",parse_dates=["Order_Date"])
# print(check2["Order_Date"].dtype)
# print(check2["Order_Date"].isna().sum())
# print(check2["Order_Date"].min())


# print(check2["Order_Date"].notna().sum())
# print(check2["Order_Date"].isna().sum())
# print(check2["Order_Date"].notna().sum() + check2["Order_Date"].isna().sum())

# print(os.path.abspath("data/cleaned_data.csv"))
print(df[["Units_Sold", "Units_Clean"]].isna().sum())