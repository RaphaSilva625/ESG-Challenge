import pandas as pd
import numpy as np
import time

#creating two functions to visualize data processing time.
#Captures current time as "beginning" of processing
def tic():
    global _start_time 
    _start_time = time.time()

#Captures current time as "end" of processing, subtracts time in seconds and converts to hour, minute and second
def tac():
    t_sec = round(time.time() - _start_time)
    (t_min, t_sec) = divmod(t_sec,60)
    (t_hour,t_min) = divmod(t_min,60) 
    print('Time passed: {}hour:{}min:{}sec'.format(t_hour,t_min,t_sec))

#Loading the data as dataframe using pandas
general_ledger_df = pd.read_excel('input\general_ledger.xlsx')
chart_accounts_df = pd.read_excel('input\chart_of_accounts.xlsx')

#Ordering the dataframe as ascending by account
general_ledger_df_sorted = general_ledger_df.sort_values(by=['account'])

#Create a function that takes an account number like str, then looks up the account in the general_ledger dataframe and sums all occurrences and return a sum as type float
def branch_sum(account_number: str) -> float:
    sum = 0.0
    for index, row in general_ledger_df_sorted.iterrows():
        if row['account'].startswith(account_number):
            sum += row['value']
    return sum


if __name__ == "__main__":
    
    #Creates a list using the map() method that apply a function on each element of my dataframe and returns an element of my list
    #Using the tic(), tac() method to see the processing time of my function
    tic()
    list_sum = list(map(branch_sum, chart_accounts_df['account']))
    tac()

    #Appends the new list to a copy of my original chart of accounts and exports the output as a csv file.
    new_chart_accounts_df = chart_accounts_df.copy()
    new_chart_accounts_df['value'] = list_sum

    #Exporting the new chart of accounts, now populated with the values.
    new_chart_accounts_df.to_csv('output\chart_of_accounts_populated.csv', index=False)