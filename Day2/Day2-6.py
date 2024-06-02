age = input("what is your current age ?")

type_age = int(age)

days = type_age * 365

weeks = days / 7

type_weeks = float(round(weeks ,1))

months = weeks / 4

type_months = float(round(months ,1))

print(f"you have {days} days, {type_weeks} weeks and {type_months} monthes left.")