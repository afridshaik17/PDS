# Loading the dataset
import pandas as pd # type: ignore

df = pd.read_csv("C:\\Users\\afrid\\Desktop\\PDS\\Assignment_1\\Frailty_Dataset\\raw_data\\frailty_data.csv")

# Display first few rows
print(df.head())

print("summary Descriptive stastics:")
summary = df.describe()

df.to_csv("frailty_data.csv", index=False)
summary.to_csv("summary_Descriptive_statistics.csv")

print(summary)