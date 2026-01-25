-- You are given the employees table:

-- Column	Type
-- id	integer
-- first_name	string
-- last_name	string
-- age	integer
-- sex	string
-- employee_title	string
-- department	string
-- salary	integer
-- targe	integer
-- bonus	integer
-- city	string
-- address	string
-- manager_id	integer
-- Find employees who are earning more than their managers. 
-- Output the employee’s first name along with their corresponding salary. 
-- Your output should have the following columns: first_name (of the employee), manager_salary.


select e.first_name, m.salary as manager_salary 
from `project.dataset.employees` e 
left join `project.dataset.employees` m on e.manager_id=m.id
where e.salary > m.salary

-- Your company has a users table that has accumulated many duplicate email addresses. Some of these duplicates are due to differences in case sensitivity, while others are due to unintentional whitespaces before or after the email. For instance, john@example.com and JOHN@EXAMPLE.COM are considered duplicates.

-- Consider the users table schema:

-- Write a SQL query that returns records from the users table while excluding any duplicate email entries. Your solution should:

-- Treat email addresses as duplicates if they match after accounting for case and whitespace
-- Include only one record for each email, keeping the record with the smallest id.
-- Return the cleaned table, ordered by id.

select min(id) as id, trim(lower(email)) as email
from users group by 2 order by id

Amazon is a large e-commerce platform where customers can order various items ranging from electronics to clothing.

-- You're provided with two tables, orders and items, with the following columns

-- order_id	customer_id	order_date	item_id	order_quantity
-- integer	integer	date	integer	integer

-- item_id	item_category
-- integer	string

-- Write a SQL query to get the second earliest order_id for each customer 
-- for each date they placed at least two orders. Your output should have the 
-- following columns: customer_id, order_date, second_earliest_order_id. 
-- Order it by order date and customer ID.

with cte as(
    select customer_id, order_date,order_id as second_earliest_order_id,
    row_number() over(partition by customer_id,order_date order by order_date asc) row_num
    from orders

)select customer_id, order_date, second_earliest_order_id from cte 
where row_num=2 order by order_date, customer_id