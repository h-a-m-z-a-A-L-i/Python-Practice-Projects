# Stock News Alert System 📈🚀

A Python application that monitors stock price movements and automatically sends news alerts via SMS when significant changes occur.

## Features
- **Stock Tracking**: Uses the Alpha Vantage API to monitor daily closing prices.
- **Volatility Alerts**: Triggers when a stock price changes by more than 5% between two consecutive days.
- **News Integration**: Fetches relevant news articles using the News API to provide context for the price movement.
- **SMS Notifications**: Sends the percentage change along with the top 3 news headlines and descriptions directly to your phone via Twilio.

## Setup Instructions

### 1. Prerequisites
- Python 3.x
- API Keys for:
  - [Alpha Vantage](https://www.alphavantage.co/support/#api-key)
  - [News API](https://newsapi.org/)
  - [Twilio](https://www.twilio.com/)

### 2. Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-news-alert.git
   cd stock-news-alert
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 3. Environment Variables
1. Copy the `.env.example` file to create a `.env` file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and fill in your API keys and Twilio credentials.

### 4. Running the App
```bash
python main.py
```

## Technologies Used
- **Python**: Core logic and automation.
- **Requests**: For API interactions.
- **Twilio SDK**: For SMS delivery.
- **Dotenv**: For secure environment variable management.
