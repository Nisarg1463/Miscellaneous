import datetime
days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
months=['january','februry','march','april','may','june','july','august','september','october','novembar','december']
extentions=['st','nd','rd','th']
days_of_month=[31,28,31,30,31,30,31,31,30,31,30,31]

def day_identifier(text):
    global days,months,extentions,days_of_month
    text=text.lower()
    today=datetime.date.today()
    year=today.year
    day=-1
    month=-1
    day_of_week=-1
    if text.count('today')>0:
        return today
    if text.count('tomorrow')>0:
        print(today.day , today.month , today.year)
        if today.day+1>days_of_month[today.month-1] and today.month!=2:
            if today.month==12:
                 return datetime.date(day=1,month=1,year=year+1)
            return datetime.date(day=1,month=today.month+1,year=year)
        elif today.month==2:
            leap_year=today.year%4==0
            if today.day+1>days_of_month[1]:
                if leap_year:
                    if today.day+1 > days_of_month[1]+1:
                        return datetime.date(day=1,month=today.month+1,year=year)
                    else:
                        return datetime.date(day=today.day+1,month=today.month,year=year)
                return datetime.date(day=1,month=today.month+1,year=year)
        return datetime.date(day=today.day+1,month=today.month,year=year)
    for words in text.split():
       if words in months:
           month=months.index(words)+1
       elif words in days:
           day_of_week=days.index(words)
       elif words.isdigit():
           day=int(words)
       else:
           for i in extentions:
               if i in words:
                   day=int(words[:words.index(i)])
    if month<today.month and month!=-1:
        year=year+1
    if day<today.day and month==-1 and day!=-1:
        month=today.month+1
    if day==-1 and month==-1 and day_of_week!=-1:
        current_day_of_week=today.weekday()
        diff=day_of_week-current_day_of_week
        if diff<=0:
            diff+=7
            if text.count('next')>0:
                diff+=7
            return today + datetime.timedelta(diff)
        return datetime.date(month=month,day=day+diff,year=year)
    return datetime.date(month=month,day=day,year=year)

print(day_identifier('monday'))