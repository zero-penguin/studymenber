import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('my-project-for-django-6373bfd9de88.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('1N9rCY6qTKw1GVsPFVKk7kXYWbPT4Lq6Mb0BgIsbLlR4').sheet1

wks.update_acell('A1', 'Hello World!')
print(wks.acell('A1'))