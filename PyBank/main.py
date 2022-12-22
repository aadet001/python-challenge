import pandas as pd 
import os


# pth = "Resources/budget_data.csv"
pth = "C:/Users/aaadetun/Downloads/python-challenge/PyBank/Resources/budget_data.csv"
df = pd.read_csv(pth)

#total number of months
totalMonths = len(df)

#net total amout of profit/losses
totalAmount = df['Profit/Losses'].sum()

#calculate change in Profit/Losses
n = len(df)
changes = []
changes.append(None)
for i in range(1,n):
    changes.append(df['Profit/Losses'][i]-df['Profit/Losses'][i-1])

# changes column added to dataframe
df['Changes'] = changes

#get average of changes
avgChange = '%.2f' % df['Changes'].mean()


# date of highest Profit/loss difference
maxDate = df['Date'][df['Changes'].idxmax()]
maxDifference = df['Changes'].max()
# date of lowest Profit/loss difference
minDate = df['Date'][df['Changes'].idxmin()]
minDifference = df['Changes'].min()

#print summary
print("Financial Analysis")
print("-------------------------")
print("Total Month: " + str(totalMonths))
print("Total: $" + str(totalAmount))
print("Average Change: $" + str(avgChange))
print("Greatest Increase in Profits: " + str(maxDate) + "($"+ str(maxDifference) +")")
print("Greatest Decrease in Profits: " + str(minDate) + "($"+ str(minDifference) +")")
print("-------------------------")