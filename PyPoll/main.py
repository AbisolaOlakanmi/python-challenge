import pandas as pd
import numpy as np


df = pd.read_csv('Resources/election_data.csv')

print(df.shape)

total_votes = df["Ballot ID"].nunique()

sub_df = df.groupby(['Candidate']).size().reset_index().rename(columns={0:'Vote Count'})

sub_df["%"] = round(100 *  sub_df["Vote Count"] / sub_df["Vote Count"].sum(),3)

print(sub_df.head())

winner = sub_df["Candidate"].loc[sub_df['%'].idxmax()]

print(winner)

file  = open("./analysis/pypoll.txt","w")#append mode
file.write("Election Results \n")
file.write("---------------------- \n")
file.write(f"Total Votes: {total_votes} \n")

file.write("---------------------- \n")


for c in range(len(sub_df)):
    file.write(f"{sub_df['Candidate'].iloc[c]} : {sub_df['%'].iloc[c]}% ({sub_df['Vote Count'].iloc[c]}) \n")


    # print(f"Candidate: {sub_df['Candidate'].iloc[c]} ")
    # print(f"% Votes: {sub_df['%'].iloc[c]} ")
    # print(f"Votes Counted: {sub_df['Vote Count'].iloc[c]} ")

file.write("---------------------- \n")

file.write(f"Winner: {winner}  \n")


file.write("---------------------- \n")

file.close()