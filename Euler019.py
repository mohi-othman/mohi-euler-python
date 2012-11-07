veryFirstSunday = (31,12,1899)

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
        
def daysBetweenDates(fromdate, todate):
    days = 0
    years = todate[2] - fromdate[2]

    if todate[2]>fromdate[2]:
        days+= daysBetweenDatesInSameYear(fromdate[0],fromdate[1],31,12,fromdate[2])              
        
        for i in range(1,years):
            if isLeapYear(i+fromdate[2]):
                days += 366
            else:
                days += 365

        days+= daysBetweenDatesInSameYear(1,1,todate[0],todate[1],todate[2])              

    else:
        days+= daysBetweenDatesInSameYear(fromdate[0],fromdate[1],todate[0],todate[1],todate[2])              
  
    return days

def daysBetweenDatesInSameYear(day1, month1, day2, month2,year):
    if month1==month2:  
        return day2-day1+1
    
    days = 0
    month = month1
    while(month<=month2):
        day = 1
        
        if month==month1:
            day = day1

        if month==month2:
            days += day2
        elif month in (9,4,6,11):
            days += 30 - day + 1            
        elif month in (1,3,5,7,8,10,12):
            days += 31 - day + 1            
        elif month == 2 and isLeapYear(year):
            days += 29 - day + 1            
        elif month == 2 and not isLeapYear(year):
            days += 28 - day + 1

        month+=1

    return days

def firstSundayAfterDate(date):
    s = daysBetweenDates(veryFirstSunday,date)-1
    dayOfWeek = s%7
    
    if dayOfWeek == 0:
        return date
    else:
        return(date[0]+(7-dayOfWeek),date[1],date[2])


def isSunday(date):
    s = daysBetweenDates(veryFirstSunday,date)-1
    dayOfWeek = s%7
    
    if dayOfWeek == 0:
        return True
    else:
        return False

    
startDate = (1,1,1901)
endDate = (31,12,2000)

month = startDate[1]
year = startDate[2]
count = 0
while(year<endDate[2] or (year==endDate[2] and month<=endDate[1])):
    if isSunday((1,month,year)):
        count+=1

    month+=1
    if month>12:
        month=1
        year+=1

print(count)
