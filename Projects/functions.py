{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}
def labor_calc():
    print('Labor Rate')
    rate = float(input())
    print('Number of men')
    men = float(input())
    print('Number of days')
    days = float(input())
    print('Overtime?')
    ot_answer = str(input().lower())

    #total hours is number of men times 10 hour working day times total number of projected days
    hours = (men*10)*days
    #add in overtime hours if there are any
    if ot_answer == 'yes':
        ot_rate = rate * 1.5
        print('Number of Overtime Days?')
        ot_days = float(input())
        ot_cost = ot_rate*(men*10)*ot_days
        
    if ot_answer == 'yes':
        total_labor_price = (hours*rate) + ot_cost
    else:
        total_labor_price = hours*rate
        
    #print total labor price
    total = print(f"Total labor price is: {total_labor_price}")
    return total

