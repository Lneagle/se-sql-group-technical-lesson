import sqlite3
import pandas as pd

conn = sqlite3.Connection('data.sqlite')

q = """
SELECT country, COUNT(*)
FROM customers
GROUP BY country
;
"""
# Displaying just the first 10 countries for readability
customers_count_by_country = pd.read_sql(q, conn).head(10)
print(customers_count_by_country)

q = """
SELECT country, COUNT(*)
FROM customers
GROUP BY 1
;
"""
# Displaying just the first 10 countries for readability
customers_count_by_country = pd.read_sql(q, conn).head(10)
print(customers_count_by_country)

q = """
SELECT country, COUNT(*) AS customer_count
FROM customers
GROUP BY country
;
"""
# Displaying just the first 10 countries for readability
customers_count_by_country = pd.read_sql(q, conn).head(10)
print(customers_count_by_country)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS INTEGER)) AS min_purchase,
   MAX(CAST(amount AS INTEGER)) AS max_purchase,
   AVG(CAST(amount AS INTEGER)) AS avg_purchase,
   SUM(CAST(amount AS INTEGER)) AS total_spent
FROM payments
GROUP BY customerNumber
;
"""

payment_summary = pd.read_sql(q, conn)

print(payment_summary)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS INTEGER)) AS min_purchase,
   MAX(CAST(amount AS INTEGER)) AS max_purchase,
   AVG(CAST(amount AS INTEGER)) AS avg_purchase,
   SUM(CAST(amount AS INTEGER)) AS total_spent
FROM payments
WHERE strftime('%Y', paymentDate) = '2004'
GROUP BY customerNumber
;
"""

payment_summary_2024 = pd.read_sql(q, conn)
print(payment_summary_2024)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS INTEGER)) AS min_purchase,
   MAX(CAST(amount AS INTEGER)) AS max_purchase,
   AVG(CAST(amount AS INTEGER)) AS avg_purchase,
   SUM(CAST(amount AS INTEGER)) AS total_spent
FROM payments
GROUP BY customerNumber
HAVING avg_purchase > 50000
;
"""

payments_over_fifty_thousand = pd.read_sql(q, conn)
print(payments_over_fifty_thousand)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS INTEGER)) AS min_purchase,
   MAX(CAST(amount AS INTEGER)) AS max_purchase,
   AVG(CAST(amount AS INTEGER)) AS avg_purchase,
   SUM(CAST(amount AS INTEGER)) AS total_spent
FROM payments
WHERE amount > 50000
GROUP BY customerNumber
HAVING number_payments >= 2
;
"""

multiple_purchase_payment_summary = pd.read_sql(q, conn)
print(multiple_purchase_payment_summary)

q = """
SELECT
   customerNumber,
   COUNT(*) AS number_payments,
   MIN(CAST(amount AS INTEGER)) AS min_purchase,
   MAX(CAST(amount AS INTEGER)) AS max_purchase,
   AVG(CAST(amount AS INTEGER)) AS avg_purchase,
   SUM(CAST(amount AS INTEGER)) AS total_spent
FROM payments
WHERE amount > 50000
GROUP BY customerNumber
HAVING number_payments >= 2
ORDER BY total_spent
LIMIT 1
;
"""

lowest_duplicate_spender = pd.read_sql(q, conn)
print(lowest_duplicate_spender)

conn.close