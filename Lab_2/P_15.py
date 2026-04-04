#check leap year using logical operator   (year%4==0andyear%100!=0)or(year%400==0)
year = int(input("Enter the year"))
print((year%4==0 and year%100!=0)or(year%400==0))