# Program to convert total days into years, months, and days
def conday():
    days = int(input("Enter total number of days: "))

    years = days // 365
    remaining_days = days % 365

    months = remaining_days // 30
    days_left = remaining_days % 30
    if years ==0 and months == 0:
        print("{} Days  ".format(days))
    elif years ==0:
        print("{} Months  ".format(months))
        print("{} Days  ".format(days_left))
    else:
     print("{} Years ".format(years))
     print("{} Months".format(months))
     print("{} Days  ".format(days_left))

conday()



