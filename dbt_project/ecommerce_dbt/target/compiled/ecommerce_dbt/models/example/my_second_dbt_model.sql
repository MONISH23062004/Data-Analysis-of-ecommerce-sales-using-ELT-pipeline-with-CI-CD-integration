-- Use the `ref` function to select from other models

select *
from ecommerce_db.raw.my_first_dbt_model
where id = 1