# python-challenge
## PyBank
The PyBank folder contains files needed to analyze the financial records which are in the file budget_data.csv in the Resources folder, which contains two columns of data: _Date_ and _Profit/Losses_. 

The PyBank folder contains the main.py file which is the python script that when run, analyzes the records within budget_data.csv. Once run, the script outputs the Financial Analysis in the terminal and in the text file analysis.txt, which is found in the Analysis folder within the PyBank folder.

The Financial Analysis contains:
- the total number of months in the dataset
- the net total amount of _Profit/Losses_ over the full period
- the changes of _Profit/Losses_ over the full period
- the average of the change of _Profit/Losses_
- the date and amount of greatest increase and decrease in _Profit/Losses_ over the entire period

## PyPoll
The PyBank folder contains files needed to analyze the election data which are in the file election_data.csv in the Resources folder, which contains three columns of data: _Ballot ID_, _County_ and _Candidate_. 

The PyPoll folder contains the main.py file which is the python script that when run, analyzes the records within election_data.csv. Once run, the script outputs the ELection results in the terminal and in the text file analysis.txt, which is found in the analysis folder within the PyPoll folder.

The Election Results contains:
- the total number of votes
- the names of all of the candidates
- the percentage of the total votes each candidate got
- the number of votes each candidate got
- the winner of the election based on the greatest number of votes

## Citations
The script in main.py in the PyBank folder and the PyPoll folder both contain codes from the following websites:
- https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
  The code from this website was used to format float variables to a certain number of decimal points, it is present in line 46 in the PyBank main.py script and in lines 50-52 in the PyPoll main.py script.

- https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-fil
  The code from this website was used to print lines to a text file instead of to the terminal, it is present in lines 81-88 in the PyBank main.py script and in lines 84-94 in the PyPoll main.py script.
