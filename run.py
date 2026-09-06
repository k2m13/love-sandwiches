import google.auth
import gspread

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

CREDS, PROJECT_ID = google.auth.default(scopes=SCOPES)

GSPREAD_CLIENT = gspread.authorize(CREDS)

SHEET = GSPREAD_CLIENT.open("love_sandwiches")

sales = SHEET.worksheet("sales")
data = sales.get_all_values()

print("Successfully connected!")
print(data)