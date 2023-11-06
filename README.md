# Python Challenge - PyBank and PyPoll

## Project Summary
Project Name: Python Challenge - PyBank and PyPoll

Objective: The goal of this project was to complete two Python challenges, PyBank and PyPoll, to analyze real-world financial and election data using Python scripting.

## Key Achievements:

Successfully created Python scripts for both PyBank and PyPoll challenges.
Analyzed financial records in PyBank to calculate total months, net profit/loss, average change, greatest increase, and greatest decrease in profits.
Modernized vote-counting in PyPoll, determining the total votes, candidates, percentage of votes won, and the election winner.
Printed analysis results to the terminal and exported results to text files.
Skills Developed:

Improved Python programming skills by working with CSV files, variables, lists, dictionaries, and loops.
Gained experience in data analysis and data manipulation using Python.
Enhanced the ability to break down complex problems into smaller, manageable tasks.

## Project instruction
Initial steps:

1. Create a new repository for this project on GitHub.
2. Clone the repository to your local computer.
3. Inside your local Git repository, create two folders: `PyBank` and `PyPoll`.
4. For each of the two folders, add the following content:

   - A new file called `main.py`. This will be the main script to run for each analysis.
   - A `Resources` folder that contains the CSV files provided in the challenge. Ensure that your script has the correct path to the CSV file.
   - An `analysis` folder that will contain the text file with the results from your analysis.

5. Push these changes to your GitHub repository to keep your work safe and accessible.

## PyBank Challenge
In the PyBank challenge, you are tasked with analyzing the financial records of a company. You will use the `budget_data.csv` dataset, which contains two columns: "Date" and "Profit/Losses". Your Python script should calculate the following values:

- Total number of months included in the dataset
- Net total amount of "Profit/Losses" over the entire period
- Changes in "Profit/Losses" over the entire period, along with the average of those changes
- Greatest increase in profits (date and amount) over the entire period
- Greatest decrease in profits (date and amount) over the entire period

Your analysis should align with the following results:

```
Financial Analysis 
---------------------------- 
Total Months: 86 
Total: $ 22564198 
Average Change: $ 262374.40 
Greatest Increase in Profits: Mar-13 ($1141840) 
Greatest Decrease in Profits: Dec-10 ($-1194133)
```

Your final script should both print the analysis to the terminal and export a text file with the results.

## PyPoll Challenge
In the PyPoll challenge, you need to help a small rural town modernize its vote-counting process. You will use the `election_data.csv` dataset, which contains three columns: "Voter ID," "County," and "Candidate." Your Python script should calculate the following values:

- Total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election based on the popular vote

Your analysis should align with the following results:

```
Election Results 
------------------------- 
Total Votes: 369711 
------------------------- 
Charles Casper Stockham: 23.049% (85213)
Diana DeGette: 73.812% (272892)
Raymon Anthony Doane: 3.139% (11606)
------------------------- 
Winner: Diana DeGette 
-------------------------
```

As with the PyBank challenge, your final script should both print the analysis to the terminal and export a text file with the results.

## Hints and Considerations
- Utilize the knowledge you've gained in previous lessons, such as importing modules like `csv`, reading and writing files, storing data in variables, lists, and dictionaries, and iterating through data structures.

- Keep in mind that the datasets for these challenges are relatively large. This is an opportunity to demonstrate the power of Python for handling big data compared to traditional Excel-based analysis.

- Write one script for each of the provided datasets. Run each script separately to ensure that the code works for its respective dataset.

- Commit your work frequently and back it up with pushes to your GitHub repository to avoid losing your progress.

- Make sure that your repository includes a detailed `README.md` file to provide information and instructions for your project.

