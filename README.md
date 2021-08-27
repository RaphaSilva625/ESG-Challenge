## ESG Challenge

#### How I thought to solve this challenge


First I tried to solve it using some pandas method like groupby 
and go back to the previous node and got this result.

account			|	value
----------------|------------
01.1.1.01.001	|	27508.42
01.1.1.01.002	|	24170.31
01.1.1.01.003	|	22302.17
01.1.1.01.004	|	25456.13
01.1.1.01.005	|	28752.79

So I would add the values by removing the final numbers from the account using some substring method, but naah this is not cool
And I wasn't using the account file for anything, so I thought of a way to make it useful and make my life easier

So I thought, I'm going to use 2 chained for to scan the general ledger table using the account numbers from the accounts table, like this.

```list_account_sum = []
for account in chart_accounts_df['account']:
    sum = 0
    for index, row in general_ledger_df_sorted.iterrows():
        if row['account'].startswith(account):
            sum += float(row['value'])
    list_account_sum.append(sum)```
	

As I hope, it worked, but I thought I could improve the look of the solution a little, make it cleaner and more reusable.
That's when I thought about creating a function, using the account number as a parameter and then using the map()
method to apply my function to each element of my list of accounts and return me the sum of the value in which that account appears.

``` def branch_sum(account_number: str) -> float:
    sum = 0
    for index, row in general_ledger_df_sorted.iterrows():
        if row['account'].startswith(account_number):
            sum += row['value']
    return float(sum)```
	
`list_sum_using_map = list(map(branch_sum, chart_accounts_df['account']))`

After processing, I created a copy of my original accounts dataframe and added a new column called value, which would be the sum of all the respective "branches" of my main account.
Exported as a new file in csv format.


Ps.: 

* I had a bit of difficulty understanding what was passed, I reread it a few times to be sure what was being asked.
* I'm pretty sure we could cut the processing time using a more complex solution, but due to the turnaround time, this is all I managed to develop, sorry about that.
* I've never used automated tests in python, this is definitely one of my weaknesses, I've always done manual or tabletop tests, this is why my unit test is pretty weak.
* it's been a while since i had so much fun working out a solution, thanks for that.
* Sorry for my english, i'm trying