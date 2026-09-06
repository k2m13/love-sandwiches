import google.auth
import gspread

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

CREDS, PROJECT_ID = google.auth.default(scopes=SCOPES)

GSPREAD_CLIENT = gspread.authorize(CREDS)

SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please provide sales data from the latest market.")
    print("Data should be six numbers, seperated by commas.")
    print("Example: 10, 20, 30, 40, 50, 60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()