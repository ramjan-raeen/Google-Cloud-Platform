USE raw_data;

CREATE TABLE dim_date (
    date_key INT NOT NULL,
    full_date DATE,
    day_of_week VARCHAR(20),
    month INT,
    month_name VARCHAR(20),
    quarter INT,
    year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (date_key)
);

CREATE TABLE dim_category (
    category_key INT NOT NULL,
    category_name VARCHAR(255),
    department VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (category_key)
);