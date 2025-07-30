SELECT
  o.order_id,
  o.order_date,
  c.customer_name,
  p.product_name,
  p.category,
  p.price,
  o.quantity,
  (p.price * o.quantity) AS total_amount
FROM {{ source('raw', 'orders') }} o
JOIN {{ source('raw', 'customers') }} c ON o.customer_id = c.customer_id
JOIN {{ source('raw', 'products') }} p ON o.product_id = p.product_id
