import yfinance as yf
import smtplib
import datetime

# =============================
# CONFIG (CHANGE THIS)

# =============================

EMAIL = "your@email.com"
APP_PASSWORD = "your_app_password"

# =============================
# GET REAL DATA
# =============================

hist = mu.history(period="6mo")

if hist is None or len(hist) < 60:
    price_change = 0
else:
    price_now = hist["Close"].iloc[-1]
    price_3mo = hist["Close"].iloc[-60]

    if price_3mo == 0:
        price_change = 0
    else:
        price_change = ((price_now - price_3mo) / price_3mo) * 100

# =============================
# SCORING SYSTEM
# =============================

cycle_score = 0

if gross_margin > 50:
    cycle_score += 2

if revenue_growth > 20:
    cycle_score += 2

if price_change < 10:
    cycle_score += 2

# =============================
# EMAIL FUNCTION
# =============================

def send_email(message):
    subject = "⚠️ Semiconductor Cycle Alert"
    msg = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.sendmail(EMAIL, EMAIL, msg)

# =============================
# LOGIC
# =============================

today = datetime.datetime.now()

if cycle_score >= 5:
    message = f"""
⚠️ LATE-CYCLE WARNING DETECTED

Score: {cycle_score}/6
Date: {today}

Gross Margin: {gross_margin:.2f}%
Revenue Growth: {revenue_growth:.2f}%
Price Change (3mo): {price_change:.2f}%
"""
    send_email(message)

