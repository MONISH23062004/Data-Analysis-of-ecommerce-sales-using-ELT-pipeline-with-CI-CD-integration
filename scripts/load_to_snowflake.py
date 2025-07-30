import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env (for local use)
load_dotenv()

# Fetch values from environment (works for both local + GitHub Actions)
user = os.getenv('SNOWFLAKE_USER')
password = os.getenv('SNOWFLAKE_PASSWORD')
account = os.getenv('SNOWFLAKE_ACCOUNT')
warehouse = 'compute_wh'
database = 'ecommerce_db'
schema = 'raw'

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=user,
    password=password,
    account=account,
    warehouse=warehouse,
    database=database,
    schema=schema
)

cursor = conn.cursor()

# Load CSV files
customers = pd.read_csv('data/customers.csv')
orders = pd.read_csv('data/orders.csv')
products = pd.read_csv('data/products.csv')

# Create tables
cursor.execute("CREATE OR REPLACE TABLE customers (customer_id INT, customer_name STRING, country STRING)")
cursor.execute("CREATE OR REPLACE TABLE orders (order_id INT, customer_id INT, product_id INT, order_date DATE, quantity INT)")
cursor.execute("CREATE OR REPLACE TABLE products (product_id INT, product_name STRING, category STRING, price FLOAT)")

# Insert data
for _, row in customers.iterrows():
    cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(row))
for _, row in orders.iterrows():
    cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", tuple(row))
cursor.execute(
    "INSERT INTO products VALUES (%s, %s, %s, %s)",
    tuple(row)
)


cursor.close()
conn.close()
print("✅ Data successfully loaded into Snowflake!")
