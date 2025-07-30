
  create or replace   view ecommerce_db.raw.order_analysis
  
  
  
  
  as (
    SELECT
  o.order_id,
  o.order_date,
  c.customer_name,
  p.product_name,
  p.category,
  p.price,
  o.quantity,
  (p.price * o.quantity) AS total_amount
FROM ecommerce_db.raw.orders o
JOIN ecommerce_db.raw.customers c ON o.customer_id = c.customer_id
JOIN ecommerce_db.raw.products p ON o.product_id = p.product_id
  );

