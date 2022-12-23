import pandas as pd 

pth = "PyBank/Resources/budget_data.csv"
# pth = "C:/Users/icanhearme/Downloads/Data Science Boot Camp/HW Assignments/challenge 3/PyBank/Resources/budget_data.csv"
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
maxDifference = '%.0f' % df['Changes'].max()
# date of lowest Profit/loss difference
minDate = df['Date'][df['Changes'].idxmin()]
minDifference ='%.0f' %  df['Changes'].min()

#print summary
print("```text")
print("Financial Analysis")
print("-------------------------")
print("Total Month: " + str(totalMonths))
print("Total: $" + str(totalAmount))
print("Average Change: $" + str(avgChange))
print("Greatest Increase in Profits: " + str(maxDate) + " ($"+ str(maxDifference) +")")
print("Greatest Decrease in Profits: " + str(minDate) + " ($"+ str(minDifference) +")")
print("```")


#write to text file
# fw = open("C:/Users/icanhearme/Downloads/Data Science Boot Camp/HW Assignments/challenge 3/PyBank/analysis/analysis.txt", "w+")
fw = open("PyBank/analysis/analysis.txt", "w+")
fw.write("```text\n")
fw.write("Financial Analysis\n")
fw.write("-------------------------\n")
fw.write("Total Month: " + str(totalMonths))
fw.write("\nTotal: $" + str(totalAmount))
fw.write("\nAverage Change: $" + str(avgChange))
fw.write("\nGreatest Increase in Profits: " + str(maxDate) + " ($"+ str(maxDifference) +")")
fw.write("\nGreatest Decrease in Profits: " + str(minDate) + " ($"+ str(minDifference) +")")
fw.write("\n```\n")

fw.close()