SELECT 1;
USE raw_data;
-- Placeholder

INSERT INTO dim_category (category_key, category_name, department)
VALUES
    (1, 'Electronics', 'Technology'),
    (2, 'Grocery', 'Food'),
    (3, 'Fashion', 'Apparel'),
    (4, 'Home & Kitchen', 'Home'),
    (5, 'Sports', 'Lifestyle');

    
INSERT INTO dim_date (
    date_key,
    full_date,
    day_of_week,
    month,
    month_name,
    quarter,
    year
)
WITH RECURSIVE dates AS (
    SELECT DATE('2026-01-01') AS d
    UNION ALL
    SELECT DATE_ADD(d, INTERVAL 1 DAY)
    FROM dates
    WHERE d < '2026-12-31'
)
SELECT
    DATE_FORMAT(d, '%Y%m%d') + 0,
    d,
    DAYNAME(d),
    MONTH(d),
    MONTHNAME(d),
    QUARTER(d),
    YEAR(d)
FROM dates;