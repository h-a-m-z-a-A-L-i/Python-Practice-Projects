from bs4 import BeautifulSoup
from smtplib import SMTP
import requests


url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'

# Define headers as amazon require certain parameters to access its web
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Upgrade-Insecure-Requests': '1'
}

# Send a request to fetch the HTML content of the page
response = requests.get(url, headers=headers)

amazon_web = response.text


sp = BeautifulSoup(amazon_web, 'html.parser')

# Get the product title
product_title = sp.find(id="productTitle").get_text().strip()

# Combine whole price and fraction for accuracy
price_whole = sp.find(class_="a-price-whole").get_text()
price_fraction = sp.find(class_="a-price-fraction").get_text()
current_price = float(f"{price_whole}{price_fraction}".replace(",", ""))

# Email Configuration (Replace with your details)
MY_EMAIL = "YOUR_EMAIL@gmail.com"
MY_PASSWORD = "YOUR_APP_PASSWORD"  # Use an App Password from Google Account
TARGET_EMAIL = "TARGET_EMAIL@gmail.com"
BUY_PRICE = 100.0

if current_price < BUY_PRICE:
    message = f"Subject:Amazon Price Alert!\n\n{product_title} is now ${current_price}!\nCheck it out here: {url}"

    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=TARGET_EMAIL,
            msg=message.encode("utf-8")
        )
    print("Price alert email sent!")
else:
    print(f"Current price is ${current_price}. Still waiting for a drop.")