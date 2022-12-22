#PyPoll
import pandas as pd 


# df = pd.read_csv("C:/Users/icanhearme/Downloads/Data Science Boot Camp/HW Assignments/challenge 3/PyPoll/Resources/election_data.csv")
df = pd.read_csv("PyPoll/Resources/election_data.csv")


#get the total number of votes cast
total_votes = len(df)

#list of candidates who received votes
candidates = df["Candidate"].unique()

n = len(df["Candidate"].value_counts())
#put all values into 2d array
#2d array default constructor. 3x3
# t = [ [0]*3 for i in range(n)]

#win percentage
winper = {}
for i in range(n): 
    winper[df["Candidate"].value_counts()[i]] = '%.3f' % (df["Candidate"].value_counts()[i]/total_votes*100)

#total number of votes for each candidate


#winner of the election
winner = df["Candidate"].value_counts().idxmax()

#print summary
print("```text")
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for i in range(n): 
    cName = df["Candidate"].value_counts().sort_index().index[i]
    cPerc = '%.3f' % (df["Candidate"].value_counts()[i]/total_votes*100)
    cVotes = df["Candidate"].value_counts()[i]
    print(cName+ ': '+ str(cPerc)+'% ('+ str(cVotes)+ ')')
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
print("```")


#write to text file
# fw = open("C:/Users/icanhearme/Downloads/Data Science Boot Camp/HW Assignments/challenge 3/PyPoll/analysis/analysis.txt", "w+")
fw = open("PyPoll/analysis/analysis.txt", "w+")
fw.write("```text\n")
fw.write("Election Results")
fw.write("\n-------------------------\n")
fw.write("Total Votes: " + str(total_votes))
fw.write("\n-------------------------\n")
for i in range(n): 
    cName = df["Candidate"].value_counts().sort_index().index[i]
    cPerc = '%.3f' % (df["Candidate"].value_counts().sort_index()[i]/total_votes*100)
    cVotes = df["Candidate"].value_counts().sort_index()[i]
    fw.write(cName+ ': '+ str(cPerc)+'% ('+ str(cVotes)+ ')\n')
fw.write("-------------------------\n")
fw.write("Winner: " + winner)
fw.write("\n-------------------------\n")
fw.write("```\n")

fw.close()
