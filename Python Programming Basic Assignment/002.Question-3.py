# Display calander of the month
import calendar


year_calander = int(input("Enter the year: "))
year_month = int(input("Enter the month: "))

print(calendar.month(year_calander, year_month))