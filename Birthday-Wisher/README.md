# Birthday Wisher

This is a small script to help you automate birthday emails for your friends and family. It checks a CSV file daily for birthdays, picks a random greeting from your templates, and sends it out automatically.

## How to use it

1.  **Set up your Gmail**: You'll need a Gmail "App Password" to let the script send emails for you. You can get one in your Google Account settings under Security (look for 2-Step Verification first).
2.  **Add your details**: Open `git.py` and replace `YOUR_EMAIL@gmail.com` and `YOUR_APP_PASSWORD` with your own email and that 16-character app password you just created.
3.  **Fill in the birthdays**: Edit `birthdays.csv` with the names, emails, and birth dates of the people you want to wish.
4.  **Run the script**:
    ```bash
    python git.py
    ```

## Files in this project

- `git.py`: The main script that does all the work.
- `birthdays.csv`: Where you store everyone's info.
- `letter_templates/`: A folder with a few different text files for your birthday messages.
- `quotes.txt`: A list of quotes (used for some extra inspiration if you want it).

## What you'll need

- Python 3
- The `pandas` library (`pip install pandas`)

