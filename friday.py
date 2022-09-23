from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os 
import time
import pyttsx3
import speech_recognition as sr

count=0
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
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
        if today.day+1>days_of_month[today.month-1] and today.month!=2:
            if today.month==12:
                 return datetime.date(day=1,month=1,year=year+1)
            return datetime.date(day=1,month=today.month+1,year=year)
        elif today.month == 2:
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
    if day<=today.day and month==-1 and day!=-1:
        month=today.month+1
    if day>today.day and month==-1:
        month=today.month
    if day==-1 and month==-1 and day_of_week!=-1:
        current_day_of_week=today.weekday()
        print(current_day_of_week)
        diff=day_of_week-current_day_of_week
        print(diff)
        if diff<=0:
            diff+=7
            if text.count('next')>0:
                diff+=7
            return today + datetime.timedelta(diff)
        return datetime.date(month=month,day=day+diff,year=year)
    return datetime.date(day=day,month=month,year=year)

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r= sr.Recognizer()
    print('listening...')
    with sr.Microphone() as source:
        audio = r.listen(source)
        said=''
        try:
            said= r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(f'Exception : {e}')
    return said

def authenticate_google():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

def get_events(n,service):
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=n, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

service=authenticate_google()
speak('Hello boss')
text=get_audio().lower()
print(day_identifier(text))
n=0
if 'hello' in text:
    speak('hello how are you?')
if 'what is your name' in text:
    speak('my name is friday')
if 'how are you' in text:
    speak("I'm fine")
if 'my schedule' in text:
    get_events(n,service)