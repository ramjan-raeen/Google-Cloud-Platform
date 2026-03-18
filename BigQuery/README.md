# BigQuery
## Introduction
BigQuery is a fully-managed, serverless data warehouse that enables scalable analysis over petabytes of data. It is designed to handle large datasets and provides fast SQL queries using the processing power of Google's infrastructure. BigQuery is part of the Google Cloud Platform and integrates seamlessly with other GCP services, making it a powerful tool for data analysis, business intelligence, and machine learning.
## Key Features
- **Serverless Architecture**: No need to manage infrastructure, allowing you to focus on analyzing data.
- **Scalability**: Automatically scales to handle large datasets and high query loads.
- **Fast SQL Queries**: Uses a distributed architecture to execute queries quickly, even on large datasets.
- **Integration with GCP**: Easily integrates with other Google Cloud services like Cloud Storage, Cloud Dataflow, and Cloud AI Platform.
- **Security**: Provides robust security features, including data encryption, access controls, and audit logging.
- **Cost-Effective**: Pay only for the storage and compute resources you use, with options for on-demand or flat-rate pricing.
## Use Cases
- **Data Warehousing**: Store and analyze large volumes of structured data.
- **Business Intelligence**: Create dashboards and reports for data-driven decision making.
- **Machine Learning**: Use BigQuery ML to build and deploy machine learning models directly within BigQuery.
- **Real-Time Analytics**: Analyze streaming data in real-time using BigQuery's integration with Cloud Dataflow and Pub/Sub.
- **Data Lake**: Use BigQuery as a data lake to store and analyze unstructured and semi-structured data.


## BigQuery Architecture
BigQuery's architecture is designed to provide high performance and scalability for data analysis. It is built on top of Google's Dremel technology, which allows for fast querying of large datasets. The architecture consists of several key components:
1. **Storage**: BigQuery uses a columnar storage format that allows for efficient storage and retrieval of data. Data is stored in a distributed manner across multiple servers, which allows for high availability and fault tolerance.
2. **Query Engine**: The query engine is responsible for executing SQL queries against the data stored in BigQuery. It uses a distributed architecture to process queries in parallel across multiple servers, which allows for fast query execution even on large datasets.
3. **Metadata Management**: BigQuery maintains metadata about the datasets, tables, and columns in the system. This metadata is used to optimize query execution and provide information about the structure of the data.
4. **Security and Access Control**: BigQuery provides robust security features, including data encryption, access controls, and audit logging. It integrates with Google Cloud Identity and Access Management (IAM) to manage permissions and access to datasets and tables.
5. **Integration with GCP Services**: BigQuery integrates seamlessly with other Google Cloud services, such as Cloud Storage for data loading and exporting, Cloud Dataflow for real-time data processing, and Cloud AI Platform for machine learning. This allows users to build end-to-end data pipelines and analytics solutions using BigQuery as the central data warehouse.
6. **User Interface**: BigQuery provides a web-based user interface in the GCP Console, as well as command-line tools and client libraries for various programming languages. This allows users to interact with BigQuery in a way that best suits their needs and preferences.
Overall, BigQuery's architecture is designed to provide a powerful and flexible platform for data analysis, allowing users to quickly and efficiently query large datasets while maintaining security and scalability.        

## Dremel tree architecture
Dremel is a query execution engine that is used by BigQuery to process SQL queries. It is based on a tree architecture, where the query is represented as a tree of operations. The tree is composed of nodes that represent different operations, such as scanning data, filtering, and aggregating results. The Dremel tree architecture allows for efficient execution of queries by breaking them down into smaller operations that can be executed in parallel across multiple servers. Each node in the tree can be executed independently, which allows for fast query execution even on large datasets. The Dremel tree architecture also enables BigQuery to optimize query execution by reordering operations and minimizing the amount of data that needs to be read from disk. Overall, the Dremel tree architecture is a key component of BigQuery's performance and scalability, allowing it to process complex SQL queries quickly and efficiently.

## What is BigQuery Execution Engine
BigQuery's execution engine is responsible for processing SQL queries and returning results. It is built on top of Google's Dremel technology, which allows for fast querying of large datasets. The execution engine uses a distributed architecture to process queries in parallel across multiple servers, which allows for fast query execution even on large datasets. When a query is submitted to BigQuery, the execution engine breaks it down into smaller operations that can be executed independently. These operations are represented as nodes in a Dremel tree, which allows for efficient execution of the query. The execution engine also optimizes query execution by reordering operations and minimizing the amount of data that needs to be read from disk. Additionally, the execution engine is designed to handle a wide range of SQL queries, including complex joins, aggregations, and subqueries. Overall, BigQuery's execution engine is a key component of its performance and scalability, allowing it to process complex SQL queries quickly and efficiently on large datasets.

## What is BigQuery Storage Engine
BigQuery's storage engine is responsible for storing and managing the data that is loaded into BigQuery. It uses a columnar storage format, which allows for efficient storage and retrieval of data. When data is loaded into BigQuery, it is automatically partitioned and distributed across multiple servers. Each partition is stored in a separate file, and the files are organized into a hierarchical structure based on the dataset and table names. This allows for fast querying of data, as BigQuery can read only the relevant partitions and files needed to answer a query, rather than scanning the entire dataset. The storage engine also uses a distributed architecture to manage the data across multiple servers, which allows for high availability and fault tolerance. Additionally, the storage engine is designed to handle a wide range of data types, including structured, semi-structured, and unstructured data. Overall, BigQuery's storage engine is a key component of its performance and scalability, allowing it to efficiently store and manage large datasets while enabling fast query performance.

## What is BigQuery Query Optimizer
BigQuery's query optimizer is a component of the execution engine that is responsible for optimizing SQL queries to improve performance. It analyzes the query and generates an execution plan that determines how the query will be executed. The query optimizer uses a variety of techniques to optimize queries, including reordering operations, minimizing the amount of data that needs to be read from disk, and choosing the most efficient join algorithms. It also takes into account the structure of the data, the size of the dataset, and the available resources to generate an optimal execution plan. The query optimizer is designed to handle a wide range of SQL queries, including complex joins, aggregations, and subqueries. By optimizing queries, the query optimizer can significantly improve query performance and reduce the amount of time it takes to return results. Overall, BigQuery's query optimizer is a key component of its performance and scalability, allowing it to efficiently process complex SQL queries on large datasets while minimizing resource usage and maximizing performance.  

## What is BigQuery Query Execution Plan
A BigQuery query execution plan is a detailed breakdown of how a SQL query will be executed by the BigQuery execution engine. It provides insights into the steps that will be taken to process the query and return results. The execution plan includes information about the operations that will be performed, such as scanning data, filtering, joining tables, and aggregating results. It also shows the order in which these operations will be executed and the resources that will be used. We can see execution plan using BigQuery UI or running dry-run, which allows users to see how their queries will be executed before actually running them. By analyzing the execution plan, users can identify potential performance bottlenecks and optimize their queries for better performance. Overall, the BigQuery query execution plan is a valuable tool for understanding how SQL queries are processed and for optimizing query performance on large datasets.


## What is Partitioning and Clustering in BigQuery
Partitioning and clustering are two techniques in BigQuery that can help improve query performance and reduce costs when working with large datasets.
- **Partitioning**: Partitioning is the process of dividing a large table into smaller, more manageable pieces called partitions. Each partition is stored separately and can be queried independently. This allows BigQuery to read only the relevant partitions when executing a query, which can significantly reduce query execution time and costs. BigQuery supports several types of partitioning, including time-based partitioning (e.g., by day, month, or year) and integer range partitioning.
- **Clustering**: Clustering is the process of organizing data within a table based on the values of one or more columns. When a table is clustered, BigQuery automatically sorts the data based on the specified clustering columns. This can improve query performance by allowing BigQuery to skip over irrelevant data when executing queries that filter on the clustering columns. Clustering is particularly effective for queries that involve range filters or equality filters on the clustering columns.
By using partitioning and clustering together, users can further optimize query performance and reduce costs in BigQuery. For example, a table can be partitioned by date and clustered by a specific column, allowing for efficient querying of data within specific date ranges while also optimizing performance for queries that filter on the clustered column. Overall, partitioning and clustering are powerful techniques in BigQuery that can help users manage and analyze large datasets more efficiently, improving query performance and reducing costs.

## What is Logical Query Processing Order
Logical Query Processing Order refers to the sequence in which SQL operations are logically executed when a query is processed. It is important to understand this order because it affects how the query is executed and how the results are produced. The logical query processing order is as follows:
1. **FROM**: The FROM clause is processed first, and it determines the source tables or datasets that will be used in the query.
2. **ON**: If there are any JOIN operations, the ON clause is processed next, which specifies the conditions for joining tables.
3. **JOIN**: The JOIN operations are processed after the ON clause, which combines rows from different tables based on the specified conditions.
4. **WHERE**: The WHERE clause is processed after the JOIN operations, which filters the rows based on the specified conditions.
5. **GROUP BY**: If there are any GROUP BY operations, they are processed next, which groups the rows based on the specified columns.
6. **HAVING**: The HAVING clause is processed after the GROUP BY operations, which filters the groups based on the specified conditions.    

# Getting Started
To get started with BigQuery, you can follow these steps:
1. **Create a BigQuery Dataset**: Use the GCP Console or `bq` command-line tool to create a dataset where your tables will reside.
2. **Load Data**: Load your data into BigQuery using various methods such as CSV, JSON, Avro, or Parquet files from Cloud Storage, or by streaming data directly into BigQuery.
3. **Run Queries**: Use SQL to query your data in BigQuery. You can run queries in the GCP Console, using the `bq` command-line tool, or through client libraries in various programming languages.
4. **Analyze Results**: Use the results of your queries for analysis, visualization, or to feed into machine learning models.
5. **Optimize Performance**: Use features like partitioning and clustering to optimize query performance and reduce costs.



## Create a BigQuery dataset
```sql
CREATE SCHEMA IF NOT EXISTS `hands-on-project.e_commerce`
OPTIONS(
  location='US',
  default_table_expiration_days=30,
  default_partition_expiration_days=15,
  max_time_travel_hours=168,
  storage_billing_model='LOGICAL',
  -- default_kms_keys='projects/hands-on-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key',
  description='e-commerce dataset'
);
```
## Alter BigQuery dataset
```sql
ALTER SCHEMA `hands-on-project.e_commerce`
SET OPTIONS(
  default_table_expiration_days=60,
  description="e-commenrce dataset for the products"
);
```
## Create a BigQuery table
```sql
CREATE TABLE IF NOT EXISTS `hands-on-project.e_commerce.orders`(
  order_id STRING NOT NULL 
    OPTIONS(description="Unique identifier for each customer order"),
  order_date DATE NOT NULL 
    OPTIONS(description="Date when the order was placed. Used for partitioning."),
  customer_id STRING NOT NULL 
    OPTIONS(description = "Customer unique identifier. Duplicated from customer.customer_id to support clustering and query performance optimization."),
  country STRING NOT NULL 
    OPTIONS(description = "Shipping country for the order. Derived from shipping_address.country and stored as a top-level column to support clustering and filtering optimization."),
  customer STRUCT<
    customer_id STRING NOT NULL OPTIONS(description="Unique ID of the customer"),
    first_name STRING OPTIONS(description="The first name of the customer"),
    last_name STRING OPTIONS(DESCRIPTION="The last name of the customer"),
    email STRING OPTIONS(description="The email address of the customer (PII)"),
    phone_numbers ARRAY<STRING> OPTIONS(description="The phone numbers of the customer")
  > NOT NULL
  OPTIONS(description="Customer personal information structure"),
  shipping_address STRUCT<
    street STRING OPTIONS(description="The street address of the customer"),
    city STRING OPTIONS(description="The city of the customer"),
    state STRING OPTIONS(description="The state of the customer"),
    postal_code STRING OPTIONS(description="The postal code of the customer"),
    country STRING OPTIONS(description="The country of the customer")
  > NOT NULL
  OPTIONS(description="Shipping address details"),
  payment_details STRUCT<
    payment_method STRING OPTIONS(description="The payment method used by the customer"),
    transaction_id STRING OPTIONS(description="The transaction ID for the payment"),
    amount FLOAT64 NOT NULL OPTIONS(description="The amount of the payment"),
    currency STRING OPTIONS(description="The currency of the payment")
  > NOT NULL
  OPTIONS(description="Payment tractions details"),
  items ARRAY<
    STRUCT<
      product_id STRING OPTIONS(description="Unique ID of the product"),
      product_name STRING OPTIONS(description="Name of the product"),
      category STRING OPTIONS(description="Category of the product"),
      quantity INT64 NOT NULL OPTIONS(description="Quantity of the product ordered"),
      unit_price FLOAT64 NOT NULL OPTIONS(description="Price per unit at the time of purchace")
    > 
  > 
  OPTIONS(description="List of the purchased items in the order"),
  order_status STRING 
    OPTIONS(description="The current status of the order ('PLACED', 'SHIPPED', 'DELIVERED', 'CANCELLED')"),
  created_timestamp TIMESTAMP
    OPTIONS(description="Record creation timestamp in the data warehouse")

)
PARTITION BY order_date
CLUSTER BY customer_id, country
OPTIONS(description="E-commerce orders table containing customer, payment, and item-level details. Partitioned by order date and clustered for optimized query performance.");
```

## Insert data into BigQuery table with nested and repeated fields
```sql
INSERT INTO `hands-on-project.e_commerce.orders`
(
  order_id,
  order_date,
  customer_id,
  country,
  customer,
  shipping_address,
  payment_details,
  items,
  order_status,
  created_timestamp
)
values(
  'ORD101',
  DATE('2026-02-22'),
  'CUST101',
  'USA',
  STRUCT(
    'CUST101',
    'Akhil',
    'Sharma',
    'akhil@gmail.com',
    ['91999999999', '918888888888']
  ),
  STRUCT(
    'MG Road',
    'Bangalore',
    'Karnataka',
    '560',
    'India'
  ),
  STRUCT(
    'CARD',
    'TXN101',
    100.00,
    'INR'
  ),
  [
    STRUCT(
      'PROD101',
      'iPhone 13',
      'Electronics',
      1,
      1000.00
    ),
    STRUCT(
      'PROD102',
      'MacBook Pro',
      'Electronics',
      1,
      2000.00
    )
  ],
  'PLACED',
  CURRENT_TIMESTAMP()
);
```
## Insert data into BigQuery table with nested and repeated fields and multiple rows
```sql
INSERT INTO e_commerce.orders (
  order_id,
  order_date,
  customer_id,
  country,
  customer,
  shipping_address,
  payment_details,
  items,
  order_status,
  created_timestamp
)
VALUES

(
  "ORD1002",
  DATE("2026-02-21"),
  "CUST002",
  "USA",

  STRUCT(
    "CUST002",
    "John",
    "Doe",
    "john.doe@email.com",
    ["5551234567"]
  ),

  STRUCT(
    "5th Avenue",
    "New York",
    "NY",
    "USA",
    "10001"
  ),

  STRUCT(
    "UPI",
    "TXN112233",
    120.75,
    "USD"
  ),

  [
    STRUCT("P300", "Keyboard", "Electronics", 1, 70.00),
    STRUCT("P301", "Headset", "Electronics", 1, 50.75)
  ],

  "SHIPPED",
  CURRENT_TIMESTAMP()
),

(
  "ORD1003",
  DATE("2026-02-20"),
  "CUST003",
  "UK",

  STRUCT(
    "CUST003",
    "Emma",
    "Watson",
    "emma@email.com",
    CAST([] AS ARRAY<STRING>)
  ),

  STRUCT(
    "Oxford Street",
    "London",
    "London",
    "UK",
    "W1D 1BS"
  ),

  STRUCT(
    "NETBANKING",
    "TXN445566",
    300.00,
    "GBP"
  ),

  [
    STRUCT("P400", "Monitor", "Electronics", 2, 150.00)
  ],

  "PLACED",
  CURRENT_TIMESTAMP()
);
```
## Update data in BigQuery table with nested and repeated fields
```sql
UPDATE `hands-on-project.e_commerce.orders`
SET shipping_address.state="London"
-- SET shipping_address.postal_code="W1D 1BS"
-- SET shipping_address.country="UK"
WHERE order_id="ORD1003";
```
## Update nested field in BigQuery table of multiple rows
```sql

UPDATE `hands-on-project.e_commerce.orders`
SET shipping_address=STRUCT(
  shipping_address.street,
  shipping_address.city,
  shipping_address.state,
  '10001',
  "USA"
  
)
WHERE order_id = "ORD1002";
```

# BigQuery view vs materialized view and authorised view
- **View**: A view is a virtual table that is defined by a SQL query. It does not store data itself but provides a way to query data from one or more tables. Views are useful for simplifying complex queries, providing a layer of abstraction, and controlling access to data. When you query a view, the underlying SQL query is executed, and the results are returned. Views do not improve query performance since they do not store data and are executed on-the-fly.
- **Materialized View**: A materialized view is a precomputed view that stores the results of a SQL query. Unlike a regular view, a materialized view is physically stored in the database and can be refreshed periodically to keep the data up-to-date. Materialized views can significantly improve query performance since they store the results of the query, allowing for faster retrieval. However, they require additional storage and maintenance to keep the data fresh.
- **Authorized View**: An authorized view is a view that is created with specific access controls to restrict who can query the underlying data. Authorized views allow you to control access to sensitive data by creating a view that only exposes certain columns or rows of the underlying tables. Users can be granted access to the authorized view without having direct access to the underlying tables, providing an additional layer of security. Authorized views are particularly useful for sharing data with external users or for enforcing data access policies within an organization. Overall, views, materialized views, and authorized views are powerful tools in BigQuery that can help simplify queries, improve performance, and control access to data based on specific use cases and requirements.

## When to use BigQuery view vs materialized view vs authorised view
- **Use a View** when you want to simplify complex queries, provide a layer of abstraction, or control access to data without needing to improve query performance. Views are ideal for scenarios where the underlying data is frequently updated, and you want to ensure that users always see the most current data when querying the view.
- **Use a Materialized View** when you need to improve query performance for frequently executed queries that involve complex calculations, aggregations, or joins. Materialized views are beneficial when the underlying data does not change frequently, or when you can tolerate some latency in data freshness. They are ideal for scenarios where you want to optimize performance for specific queries while accepting the trade-off of additional storage and maintenance overhead.
- **Use an Authorized View** when you need to control access to sensitive data by creating a view that only exposes certain columns or rows of the underlying tables. Authorized views are particularly useful for sharing data with external users or for enforcing data access policies within an organization. They allow you to grant access to the authorized view without giving direct access to the underlying tables, providing an additional layer of security. Authorized views are ideal for scenarios where you want to restrict access to specific data while still allowing users to query and analyze the data through the view. Overall, the choice between using a view, materialized view, or authorized view in BigQuery depends on your specific use case, performance requirements, and data access control needs.  

## Conclusion
BigQuery is a powerful and flexible data warehouse solution that can handle a wide range of data analysis needs. Whether you're looking to perform simple SQL queries or build complex machine learning models, BigQuery provides the tools and infrastructure to help you get insights from your data quickly and efficiently. With its serverless architecture and seamless integration with other GCP services, BigQuery is an excellent choice for organizations looking to leverage the power of big data analytics in the cloud.