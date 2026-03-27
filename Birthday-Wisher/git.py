import random
import pandas as pd
import datetime as dt
import smtplib

# --- CONFIGURATION ---
MY_MAIL = "YOUR_EMAIL@gmail.com"
PASSWORD = "YOUR_APP_PASSWORD"
PLACEHOLDER = "[NAME]"

# Get current date
now = dt.datetime.now()
month = now.month
day = now.day

# Load birthday data
try:
    data = pd.read_csv("birthdays.csv")
    df = pd.DataFrame(data)
except FileNotFoundError:
    print("Error: birthdays.csv not found!")
    exit()

# Check for birthdays today
for _, row in df.iterrows():
    if row["month"] == month and row["day"] == day:
        name = row["name"]
        email = row["email"]
        
        # Pick a random letter template
        letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
        chosen_letter = random.choice(letters)
        
        try:
            with open(chosen_letter, "r") as letter_file:
                content = letter_file.read()
                personalized_letter = content.replace(PLACEHOLDER, name)
                
            # Send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user=MY_MAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_MAIL,
                    to_addrs=email,
                    msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
                )
            print(f"Birthday email sent to {name} at {email}!")
            
        except FileNotFoundError:
            print(f"Error: {chosen_letter} not found!")
