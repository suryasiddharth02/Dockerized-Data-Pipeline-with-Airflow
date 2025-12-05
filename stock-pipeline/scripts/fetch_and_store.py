import os
import requests
import psycopg2  # pyright: ignore[reportMissingModuleSource]
from psycopg2.extras import RealDictCursor  # pyright: ignore[reportMissingModuleSource]

def fetch_and_store_stock_data():
    api_key = os.getenv("STOCK_API_KEY")
    stock_symbols = ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
    base_url = "https://www.alphavantage.co/query"

    try:
        response = requests.get(url, timeout=10)  # pyright: ignore[reportUndefinedVariable]
        response.raise_for_status()
        data = response.json().get("Global Quote", {})

        if not data:
            print("No data found in the API response")
            return

        price = float(data.get("05. price", 0.0))
        volume = int(data.get("06. volume", 0))

    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    try:
        conn = psycopg2.connect(
            host="postgres",
            database=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
        )
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS stock_data (
                id SERIAL PRIMARY KEY,
                symbol VARCHAR(10),
                price NUMERIC,
                volume BIGINT,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cur.execute(
            "INSERT INTO stock_data (symbol, price, volume) VALUES (%s, %s, %s)", (symbol, price, volume)  # pyright: ignore[reportUndefinedVariable]
        )

        conn.commit()
        cur.close()
        conn.close()

        print("Stock data inserted successfully")
    
    except Exception as e:
        print(f"Database error: {e}")