import calendar

print(calendar.calendar(2020))



leap=calendar.isleap(2020)
print(leap)


#finding leap days
leap_days=calendar.leapdays(2000,2020)
print(leap_days)