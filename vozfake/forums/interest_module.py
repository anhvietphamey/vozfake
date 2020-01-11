import numpy as np
import pandas as pd
from pandas.tseries.offsets import Day
from datetime import date, timedelta
from decimal import Decimal

#lịch trả nợ với số dư giảm dần
def loanRepayment(start_principal,start_date,ir,periods):
	#create an array of payment dates
	#not accept start_date = 30th
	pay_days = pd.date_range(start_date,periods = periods, freq = 'M') + Day(start_date.day)

	ir = float(ir) #explicitly forced conversion to float from whatever numeric type
	
	#create an array of date intervals
	intervals = np.array([])
	#convert timestamp to date
	t1_timestamp = pay_days[0]
	t1_date = date(t1_timestamp.year,t1_timestamp.month,t1_timestamp.day)

	#the first interval is from start_date to the first payment date
	i1 = (t1_date-start_date).days #type:float
	intervals = np.append(intervals,[i1])
	for i in range(len(pay_days)-1):
		delta = pay_days[i+1] - pay_days[i]
		intervals = np.append(intervals,[delta.days]) #type: float

	#create array of decreasing principals
	monthly_principal = start_principal/periods #step
	decreasing_principals = np.around(np.arange(start_principal,0,-monthly_principal)) #type: float


	#monthly interest payments 
	interest_table = np.around(intervals/365 * ir * decreasing_principals)

	#total monthly payment 
	monthly_payments = interest_table + monthly_principal

	#ending balance
	ending_principals = decreasing_principals - round(monthly_principal)

	#create data frame
	schedule = pd.DataFrame({
		'Date':pay_days,
		'Opening principal':decreasing_principals.astype(int),
		'Monthly interest':interest_table.astype(int),
		'Monthly payment': monthly_payments.astype(int),
		'Ending principal': ending_principals.astype(int)
		})

	return schedule
