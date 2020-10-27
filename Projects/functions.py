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



def ephesus_labor():
    # initialize cost variables
    base_drilling = 300
    extra_drilling = 100
    
    base_lift = 600
    extra_lift = 237.50
    
    #concrete and pier costs based on a standard 24" wide x 10' deep hole
    base_concrete = 225
    extra_concrete = 225
    
    base_pier = 1590.50
    extra_pier = 1590.50
    
    lights_labor = 135
    extra_lights = 135
    
    #declare independent variables
    print('Pole Height?')
    pole_height = int(input())
    
    print('Number of men on the job?')
    men = int(input())
    
    print('Labor rate?')
    labor_rate = float(input())
    
    print('Number of days?')
    days = int(input())

    print('Number of Poles?')
    poles = int(input())
    
    print('Number of Lights?')
    lights = int(input())
    
    print('Pier Base?')
    base = str(input().lower())
    
    print('Will the piers be subbed out?')
    sub = str(input().lower())
    
    
    # Calculate labor total
    if poles > 1 and pole_height <= 60:
        #calculate drilling and man labor
        drilling_cost = base_drilling + (poles*extra_drilling)
        labor_poles = ((labor_rate*10)*days)*men
        
        #calculate lift cost
        if days >= 1:
            lift_cost = base_lift + (extra_lift*days)
        else:
            lift_cost = base_lift
        
        #calculate pier base or concrete cost
        if base == 'no' and sub == 'no':
            concrete_cost = base_concrete + (extra_concrete*poles)
        elif base == 'yes' and sub == 'no':
            concrete_cost = base_pier + (extra_pier*poles)
        elif base == 'no' and sub =='yes':
            concrete_cost = 0
        else:
            concrete_cost = 0
        
        #calculate lighting labor cost
        if lights > 1:
            lighting_cost = lights_labor + (extra_lights*lights)
        else:
            print('Yo why they only installing one light, do this math in your head man')
        
        
    elif poles > 1 and pole_height > 60:
        
        #calculate drilling and man labor
        drilling_cost = base_drilling + (poles*extra_drilling)
        labor_poles = ((labor_rate*10)*days)*men
        
        #calculate lift cost
        if days >= 1:
            lift_cost = (base_lift + (extra_lift*days))*1.5
        else:
            lift_cost = base_lift*1.5
            
        #calculate pier base or concrete cost
        if base == 'no' and sub == 'no':
            concrete_cost = base_concrete + (extra_concrete*poles)
        elif base == 'yes' and sub == 'no':
            concrete_cost = base_pier + (extra_pier*poles)
        elif base == 'no' and sub == 'yes':
            concrete_cost = 0
        else:
            concrete_cost = 0
            
        #calculate lighting labor cost
        if lights > 1:
            lighting_cost = lights_labor + (extra_lights*lights)
        else:
            print('Yo why they only installing one light, do this math in your head man')
            
    elif poles == 1 and pole_height <= 60:
        drilling_cost = base_drilling
        labor_poles = ((labor_rate*10)*days)*men
        lift_cost = base_lift
        if base == 'no' and sub == 'no':
            concrete_cost = base_concrete
        elif base == 'yes' and sub == 'no':
            concrete_cost = base_pier
        elif base == 'no' and sub == 'yes':
            concrete_cost = 0
        else:
            concrete_cost = 0
        
        if lights > 1:
            lighting_cost = lights_labor + (extra_lights*lights)
        else:
            print('Yo why they only installing one light, do this math in your head man')
            
            
    elif poles == 1 and pole_height > 60:
        drilling_cost = base_drilling
        labor_poles = ((labor_rate*10)*days)*men
        lift_cost = base_lift*1.5
        if base == 'no' and sub == 'no':
            concrete_cost = base_concrete
        elif base == 'yes' and sub == 'no':
            concrete_cost = base_pier
        elif base == 'no' and sub == 'yes':
            concrete_cost = 0
        else:
            concrete_cost = 0
            
        if lights > 1:
            lighting_cost = lights_labor + (extra_lights*lights)
        else:
            print('Yo why they only installing one light, do this math in your head man')
            
            
    else:
        print("I don't know how to calculate that for you")
        
    total_price = drilling_cost + labor_poles + lift_cost + concrete_cost + lighting_cost    
    total = print(f"Total install price for this project is {total_price}")
    
    return total