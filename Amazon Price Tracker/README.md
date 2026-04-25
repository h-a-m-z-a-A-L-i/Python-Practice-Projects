# 🛒 Amazon Price Tracker

A lightweight, automated Python script designed to monitor Amazon product prices and notify you via email when a deal is found. Perfect for tracking discounts on items like the Instant Pot, electronics, or any other Amazon products.

## ✨ Features
- **Live Scraping:** Uses `BeautifulSoup4` and `Requests` to fetch real-time pricing data from Amazon.
- **Automated Alerts:** Integrated with `smtplib` to send instant email notifications when the price falls below your target budget.
- **Customizable:** Easily track any Amazon product by simply swapping the URL and setting your desired buy price.
- **Header Optimization:** Includes custom headers to ensure reliable access to Amazon's web data.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Core Libraries:** 
  - `BeautifulSoup4` (Web Scraping)
  - `Requests` (HTTP Requests)
  - `SMTPLib` (Email Integration)

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python installed. You will also need to install the following libraries:
```bash
pip install requests beautifulsoup4
```

### 2. Configuration
Open `main.py` and update the following placeholders:
- `MY_EMAIL`: Your Gmail address.
- `MY_PASSWORD`: Your Google **App Password** (Not your regular password).
- `TARGET_EMAIL`: Where you want to receive the alert.
- `BUY_PRICE`: The price threshold for the alert.

### 3. Usage
Run the script manually or set it up as a cron job/task scheduler to monitor prices daily:
```bash
python main.py
```

## ⚠️ Important Note on Gmail
To use the email feature, you must:
1. Enable **2-Factor Authentication** on your Google Account.
2. Generate an **App Password** (Select 'Mail' and 'Other' for the device name).
3. Use that 16-character code as your `MY_PASSWORD`.

---
*Disclaimer: This project is for educational purposes only. Please refer to Amazon's Conditions of Use regarding automated data collection.*
