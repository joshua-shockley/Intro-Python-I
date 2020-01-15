"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime
# variables
date = datetime.now()
# print(date)
yr = int(date.year)
mnth = int(date.month)
#print(yr, mnth)
# print(sys.argv)
# print(len(sys.argv))

if len(sys.argv) == 1:
    def make_cal(yr, mnth):
        print(calendar.month(yr, mnth))
    make_cal(yr, mnth)
if len(sys.argv) == 2:
    if len(sys.argv[1]) == 1 or len(sys.argv[1]) == 2:
        mth = int(sys.argv[1])
        print(calendar.month(yr, mth))
    elif len(sys.argv[1]) == 4:
        yar = int(sys.argv[1])
        print(calendar.month(yar, mnth))
if len(sys.argv) == 3:
    if len(sys.argv[1]) == 1 or len(sys.argv[1]) == 2:
        mth = int(sys.argv[1])
        yar = int(sys.argv[2])
        print(calendar.month(yar, mth))
    elif len(sys.argv[1]) == 4:
        yar = int(sys.argv[1])
        mth = int(sys.argv[2])
        print(calendar.month(yar, mth))
else:
    print("")
    print(" there were just too many entries or format didn't follow the following")
    print(' file month [year]')
    print('')
