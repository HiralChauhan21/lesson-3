# calculating present_days
working_days= int(input("enter the total number of working days: "))
absent_days= int(input("enter the total number of days you were absent: "))
present_days= working_days-absent_days

#calculating the percentage of present days
present_percent= int((present_days / working_days)*100)
print("the percent of days you were present is: ", present_percent, "%")

#calculating the eligibility
if present_percent >= 75:
    print("you are eligible to give the examination")
else:
    print("sorry, you are not eligible for the examination")
