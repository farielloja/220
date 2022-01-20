"""
Joseph Fariello
Lab1.py

This program completes lab 1

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def monthly_interest():
    print("This program calculates the monthly interest")
    print("on a credit card account.")
    interest_rate = eval(input("Enter the annual interest rate:"))
    billing_cycle = eval(input("Enter the number of days in billing cycle:"))
    net_balance = eval(input("Enter the net balance:"))
    pmt = eval(input("Enter the payment amount:"))
    day = eval(input("Enter the day of the cycle the payment was made:"))
    step1 = net_balance * billing_cycle
    step2 = pmt * (billing_cycle - day)
    step3 = step1 -step2
    avg_daily_balance = step3 / billing_cycle
    print("Your average daily balance is $", avg_daily_balance)
    monthly_interest = ((avg_daily_balance * interest_rate) / 12) / 100
    print("Your monthly interest is $", monthly_interest)

monthly_interest()
