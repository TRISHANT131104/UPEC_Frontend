import datetime
from datetime import date


def getdate():
    today = date.today()
    day = today.day
    mydate = datetime.datetime.now()
    month = mydate.strftime("%B")
    year = today.year
    if day == 1 or day == 21 or day == 31:
        current_day = f"{day}st {month} {year}"
    elif day == 3 or day == 23:
        current_day = f"{day}rd {month} {year}"
    else:
        current_day = f"{day}th {month} {year}"
    return current_day


def gettime():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if int(current_time[0:2]) > 12:
        current_time = str((int(current_time[0:2]) - 12)) + current_time[2:] + " pm"
    elif int(current_time[0:2]) == 12:
        current_time = str(current_time[0:2]) + current_time[2:] + " pm"
    elif int(current_time[0:2]) == 24:
        current_time = str((int(current_time[0:2]) - 12)) + current_time[2:] + " am"
    else:
        current_time = str(current_time) + " am"
    return current_time
