📈 Dockerized Stock Market Data Pipeline (Airflow + PostgreSQL)

A fully containerized ETL pipeline that automatically fetches stock market data, processes it, and stores it in PostgreSQL — all orchestrated with Apache Airflow, running entirely inside Docker Compose.

This project is designed for reliability, modularity, and easy deployment.

🚀 Features

Dockerized orchestration using Airflow

Automated scheduled pipeline (daily or hourly)

Fetches real-time stock data from Alpha Vantage (or optional Yahoo Finance)

Parses JSON response and stores data in a PostgreSQL table

Environment variables for secure secrets management

Built-in error handling and retry logic

Persistent database storage

Clean, scalable project structure

📁 Project Structure
.
├── docker-compose.yml
├── .env
├── dags/
│   └── stock_pipeline_dag.py
├── scripts/
│   └── fetch_and_store.py
└── README.md

🛠️ Prerequisites

You must have installed:

Docker

Docker Compose

Internet connection (to fetch stock API data)

Verify:

docker --version
docker compose version

🔧 Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Create a .env File

In your project root, create .env containing:

POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=stock_pipeline

STOCK_API_KEY=YOUR_ALPHA_VANTAGE_KEY
FERNET_KEY=YOUR_GENERATED_FERNET_KEY

Get an Alpha Vantage API key (free)

👉 https://www.alphavantage.co/support/#api-key

Generate a Fernet Key

Airflow requires this for encryption:

python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"

3️⃣ Start the Entire Pipeline

Build + start all services:

docker compose up --build


This will:

Start PostgreSQL

Initialize Airflow DB

Create Airflow admin user

Start Webserver + Scheduler

Load your DAG

🌐 Airflow Web UI

Once running, open:

👉 http://localhost:8080

Default Credentials:

Username: admin

Password: admin

▶️ Running the Stock Pipeline

Inside Airflow:

Find the DAG: stock_pipeline_dag

Toggle it ON

Click ▶ Run to trigger manually OR wait for scheduled time

📊 Viewing Stored Stock Data

Connect to PostgreSQL inside Docker:

docker exec -it postgres psql -U airflow -d stock_pipeline


Query the table:

SELECT * FROM stock_data;

🧹 Stopping & Cleaning Up

To stop all containers:

CTRL + C
docker compose down


To remove containers + database data:

docker compose down -v

🐛 Troubleshooting
❌ Airflow exited with code 1

✔ Likely wrong Fernet key or DB issue
✔ Try deleting volumes:

docker compose down -v
docker compose up --build

❌ Airflow UI not opening

Check port:

lsof -i :8080

🧩 Optional: Yahoo Finance Version (No API Key Needed)

If you prefer a version without API keys, replace the fetch script with:

import yfinance as yf


Ask and I will generate the full Yahoo-Finance version.

📜 License

MIT License — free to use, modify, and distribute.

🙌 Contribution

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.
