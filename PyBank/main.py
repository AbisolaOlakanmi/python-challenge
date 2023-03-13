import pandas as pd
import numpy as np


df = pd.read_csv('Resources/budget_data.csv', parse_dates=['Date'])

print(df.head())


file  = open("./analysis/pybank.txt","w")# write mode
file.write("Financial Analysis \n")
file.write("---------------------- \n")

total_months= df["Date"].nunique()
total = df['Profit/Losses'].sum()
df["Changes"] = df["Profit/Losses"].diff().replace(np.nan,0)
average = round(df["Changes"].sum()/(len(df["Changes"])-1),2)


great_inc = (df["Date"].loc[df["Changes"].idxmax()],df["Changes"].max())



great_dec = (df["Date"].loc[df["Changes"].idxmin()],df["Changes"].min())

print(df.head())



file.write(f"Total months: {total_months} \n")

file.write(f"Total sum of Profits/Losses: ${total} \n")



file.write(f"Average Change: {average} \n")






file.write(f"Greatest Increase in Profits: {great_inc[0]} ($ {great_inc[1]}) \n")

file.write(f"Greatest Decrease in Profits: {great_dec[0]} ($ {great_dec[1]}) \n")

file.close()

print("Done")