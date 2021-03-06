"""
birthday.py
Author: Adam Glueck
Credit: None
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
#hastag
todaydate = datetime.today().day
monthtoday = month_name[todaymonth]
name = input("Hello, what is your name? ")
Hi= " Hi " 
n =", what was the name of the month you were born in? "
month=input(Hi+name+n)
c = "And what year were you born in, "
d= "? "
#whatevs
year=int(input(c+name+d))
day =int(input("And the day? "))
if month=="December" or month=="January" or month=="February":
    season="winter"
if month=="March" or month=="April" or month=="May":
    season="spring"
if month=="June" or month=="July" or month=="August":
    season="summer"
if month=="September" or month=="October" or month=="November":
    season="fall"
if year<1980:
    era="Stone Age."
if year>1979 and year<1990:
    era="eighties."
if year>1989 and year<2000:
    era="nineties."
if year>1999 and year<2017:
    era="two thousands."
if year>2016:
    era="the future."
text=", you are a "
baby=" baby of the "
if day==todaydate and monthtoday==month:
    print("Happy birthday!")
else:
    if day==31 and month=="October":
        print("You were born on Halloween!")
    else:
        print(name+text+season+baby+era)
