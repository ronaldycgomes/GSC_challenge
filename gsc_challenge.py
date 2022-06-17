from datetime import datetime, timedelta
import json
import requests as requests
import pandas as pd

#inputs and warnings to user.
print('Please, input the dates in brazilian format: %dd/%mm/%yy')
print('Please, input the start date.', end= '\n\n')
start_date = str(input())
print('Please, input the end date.', end= '\n\n')
end_date   = str(input())
print('Please input the capital value.', end= '\n\n')
capital = float(input())
print('Please input the frequency: "day", "month", or "year".', end= '\n\n')
frequency = str(input())

###case day.
#logic to put the 'start_date' and 'end_date' in the URL.
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=dd/mm/yy&dataFinal=dd/mm/yy'
url_mod = url.replace('Inicial=dd/mm/yy', 'Inicial=' + start_date)
final_url = url_mod.replace('Final=dd/mm/yy', 'Final=' + end_date)

#consulting the API and putting the data in a df.
df = pd.read_json(final_url)

#validating first date. 
converted_start_date = datetime.strptime(start_date, '%d/%m/%y').date()
first_df_date = df.data[0]
converted_first_df_date = datetime.strptime(first_df_date, '%d/%m/%Y').date()
if(converted_start_date != converted_first_df_date):
    df = df.drop(0)
    total_days = df.index[-1] 
else:
    total_days = df.index[-1] + 1

#calculating capital 'column'.
capital_column = [] 
accrued_rates = []
rate = 1

for n in range(0, total_days):
    if(n == 0):
        accrued_rates.insert(0,0)
    else:
        calc_rate = float(df.valor[n])
        rate = rate * ((calc_rate/100) + 1)
        accrued_rates.insert(n, rate)
for i in range(0, total_days):
    if(i == 0):
        capital_column.insert(0, capital)
    else:
        capital_column.insert(i, (capital * accrued_rates[i]))

#adding the capital column to the df.
df['capital'] = capital_column

#creating 'amount earned' column.
amount_earned =[]
for i in range(0, total_days):
    if(i == 0):
        amount_earned.insert(i, 0)
    else:
        amount_earned.insert(i, capital_column[i] - capital)

#adding the 'amount earned' column to the df.
df['amount earned'] = amount_earned

#converting "data column" data from string to datetime.
df["data"] = pd.to_datetime(df["data"], format= '%d/%m/%Y')


if(frequency == 'day'):
    #Outputing the result.
    del df['valor']
    display(df)

###case month.
elif(frequency == 'month'):
    
    #getting the lists for the "month" df in order to create a df from lists.
    dates = []
    monthly_capital = []
    monthly_amount_earned = []
    end_date_converted = pd.to_datetime(end_date, format= '%d/%m/%y')
    
    if(converted_start_date != converted_first_df_date):
        for i in range(1, total_days + 1):
            if(i == total_days):
                dates.insert(i, df.data[i])
                monthly_capital.insert(i, df.capital[i])
                monthly_amount_earned.insert(i, df.loc[i].at['amount earned'])
            else:
                actual_month = (df.data[i]).month
                tomorrow_month = (df.data[i+1]).month
                if(tomorrow_month != actual_month):
                    dates.insert(i, df.data[i])
                    monthly_capital.insert(i, df.capital[i])
                    monthly_amount_earned.insert(i, df.loc[i].at['amount earned'])
                    
        #creating the monthly df and displaying it.            
        monthly_df = pd.DataFrame(dates, columns = ['data'])
        monthly_df['capital'] = monthly_capital
        monthly_df['amount earned'] = monthly_amount_earned    
        display(monthly_df)
                    
    else:
        for i in range(0, total_days):
            if(i == (total_days-1)):
                dates.insert(i, df.data[i])
                monthly_capital.insert(i, df.capital[i])
                monthly_amount_earned.insert(i, df.loc[i].at['amount earned'])
            else:
                actual_month = (df.data[i]).month
                tomorrow_month = (df.data[i+1]).month
                if(tomorrow_month != actual_month):
                    dates.insert(i, df.data[i])
                    monthly_capital.insert(i, df.capital[i])
                    monthly_amount_earned.insert(i, df.loc[i].at['amount earned'])
                    
        #creating the monthly df and displaying it.            
        monthly_df = pd.DataFrame(dates, columns = ['data'])
        monthly_df['capital'] = monthly_capital
        monthly_df['amount earned'] = monthly_amount_earned    
        display(monthly_df)
        
###case year.       
elif(frequency == 'year'):

    #getting the lists for the "yearly" df.
    dates = []
    yearly_capital = []
    yearly_amount_earned = []
    end_date_converted = pd.to_datetime(end_date, format= '%d/%m/%y')
    
    if(converted_start_date != converted_first_df_date):
        for i in range(1, total_days + 1):
            if(i == total_days):
                dates.insert(i, df.data[i])
                yearly_capital.insert(i, df.capital[i])
                yearly_amount_earned.insert(i, df.loc[i].at['amount earned'])
            else:
                actual_year = (df.data[i]).year
                tomorrow_year = (df.data[i+1]).year
                if(tomorrow_year != actual_year):
                    dates.insert(i, df.data[i])
                    yearly_capital.insert(i, df.capital[i])
                    yearly_amount_earned.insert(i, df.loc[i].at['amount earned'])
                    
        #creating the yearly df and displaying it.            
        yearly_df = pd.DataFrame(dates, columns = ['data'])
        yearly_df['capital'] = yearly_capital
        yearly_df['amount earned'] = yearly_amount_earned    
        display(yearly_df)
                    
    else:
        for i in range(0, total_days):
            if(i == (total_days-1)):
                dates.insert(i, df.data[i])
                yearly_capital.insert(i, df.capital[i])
                yearly_amount_earned.insert(i, df.loc[i].at['amount earned'])
            else:
                actual_year = (df.data[i]).year
                tomorrow_year = (df.data[i+1]).year
                if(tomorrow_year != actual_year):
                    dates.insert(i, df.data[i])
                    yearly_capital.insert(i, df.capital[i])
                    yearly_amount_earned.insert(i, df.loc[i].at['amount earned'])
       
        #creating the yearly df and displaying it.            
        yearly_df = pd.DataFrame(dates, columns = ['data'])
        yearly_df['capital'] = yearly_capital
        yearly_df['amount earned'] = yearly_amount_earned    
        display(yearly_df)
