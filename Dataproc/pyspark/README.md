# 🔍 1️⃣  What Hadoop (MapReduce) Does

Before Spark came, Hadoop was the main system for big data processing.
It has two main components:

| Component	| Description|
-------------|-------------|
| HDFS (Hadoop Distributed File System)|	Stores huge data files across multiple machines in a cluster.|
| MapReduce	| A programming model for processing data in batches. It divides work into “map” and “reduce” stages.|

🧠 Example:
If you want to count words in 100 TB of text:

Map step → breaks data into chunks and counts words per chunk.

Reduce step → combines results to get final counts.

## ✅ Pros:

Handles massive data volumes (petabytes).

Fault-tolerant — if a node fails, data can be reprocessed from HDFS.

Works well for batch processing.

## ❌ Cons:

Slow — because it writes to disk between each map and reduce stage.

Hard to program — MapReduce code is verbose and low-level (Java-based).

Not good for real-time or iterative algorithms like ML.

# ⚡ 2️⃣ What Apache Spark Does Differently

Apache Spark was created to overcome those exact problems.
It’s a unified engine for large-scale data processing — much faster, flexible, and easier to use.


## ✨ Key Features:

|Feature	|Spark	|Hadoop (MapReduce)|
|----------|-------|-------------------|
|Speed	|Up to 100× faster (in-memory computation)	|Writes to disk between steps — very slow|
|Ease of use	|APIs in Python, Scala, Java, R	|Mostly Java-based, verbose|
|Data processing types	|Batch, streaming, ML, graph, SQL (all in one engine)	|Batch only|
|In-memory	|Yes — uses RDD and caching	|No, relies on disk|
|Iterative computation	|Very efficient	|Re-reads data from disk each time|
|Streaming support	|Yes (Structured Streaming)	|No|
|Machine Learning	|MLlib library built-in	|Needs external tools|

# 🧩 3️⃣ The Core Spark Concepts
| Concept	| Meaning |
------------|------------------|
| RDD (Resilient Distributed Dataset)	|Immutable, distributed collection of objects that can be processed in parallel.
| DataFrame / Dataset	|High-level APIs for working with structured data (SQL-like).
| Catalyst Optimizer	|Optimizes SQL and DataFrame queries automatically.
| Tungsten Engine	|Manages memory and execution for speed and efficiency.
| Lazy Evaluation	|Spark builds a logical plan first, then executes efficiently when action is called.

# 🚀 4️⃣ Why Spark Outperforms Hadoop
- In-Memory Processing

    -  Spark keeps data in RAM during computation.

    - Hadoop writes every stage’s output to disk.

    - Result → Spark can be up to 100x faster for iterative tasks.

- Unified Framework

    - You can do all this in one Spark ecosystem:

    - Spark SQL → for structured queries.

    - Spark Streaming → for real-time data.

    - MLlib → for machine learning.

    - GraphX → for graph analytics.

    - Hadoop only provides MapReduce — other tools (like Pig, Hive, Mahout) must be added separately.

- Ease of Use

    - Spark provides simple APIs (Python, Scala, Java).

    - You can write a few lines of code for complex transformations.

    - Hadoop MapReduce code can be hundreds of lines long.

- Cost and Resource Efficiency

    - Spark can reuse data in memory across multiple operations.

    - Hadoop re-reads the same data from disk multiple times.

    - Hence, Spark uses resources more efficiently.

-  Real-Time + Batch

    - Spark handles streaming + batch processing.

    - Hadoop → batch only (no real-time).

# ⚙️ 5️⃣ When Hadoop is Still Useful

Spark doesn’t completely replace Hadoop.
Hadoop’s HDFS and YARN are still widely used.

👉 In fact, many Spark clusters run on top of Hadoop using its HDFS for storage and YARN for resource management.

So the relationship looks like this:

```
+--------------------------+
|      Apache Spark        |
| (processing framework)   |
+-----------+--------------+
            |
            v
+--------------------------+
|   Hadoop HDFS + YARN     |
| (storage + resource mgr) |
+--------------------------+
```

# 🧮 6️⃣ Example: Word Count Comparison
- Hadoop MapReduce (simplified Java):
```java
map(String key, String value):
    for each word in value:
        emit(word, 1)

reduce(String key, Iterator values):
    sum = 0
    for each value in values:
        sum += value
    emit(key, sum)
```

- Spark (Python):
```python
text = sc.textFile("input.txt")
counts = text.flatMap(lambda line: line.split(" ")) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b)
counts.saveAsTextFile("output")
```
💥 Simpler, faster, and cleaner.

# 📈 7️⃣ Real-World Use Cases
|Use Case|	Why Spark is Used|
|---------|------------------|  
|ETL Pipelines|	Faster transformations on massive datasets|
|Streaming Analytics|	Real-time data from Kafka or Flume|
|Machine Learning|	In-memory iterative algorithms|
|Interactive Data Analysis|	Spark SQL for ad-hoc queries|
|Data Integration|	Works with Hadoop, Hive, BigQuery, etc.|

# 8️⃣ BigData / Distributed System
## 1. What are the pros and cons of using Spark vs. Hadoop MapReduce?
| **Aspect**              | **Spark**                                        | **Hadoop MapReduce**                             |
| ------------------- | ------------------------------------------------ | ------------------------------------------------ |
| **Performance**     | In-memory processing → faster (10x–100x)         | Disk-based → slower                              |
| **Ease of Use**     | High-level APIs (Python, Scala, SQL, DataFrames) | Low-level Java APIs                              |
| **Latency**         | Suitable for batch and real-time streaming       | Suitable only for batch jobs                     |
| **Fault Tolerance** | Uses DAG + lineage to recover lost data          | Intermediate data is written to disk → resilient |
| **Resource Usage**  | More RAM needed due to in-memory model           | Uses more disk I/O, less RAM                     |
| **Deployment**      | Can run on YARN, Kubernetes, Mesos               | Primarily YARN                                   |


✅ Summary: Spark is better for most modern workloads due to speed and flexibility. MapReduce is rarely used today except in legacy systems.

## 2. How do you optimize a Spark job (e.g. partitioning, caching, shuffles)?
**🔹 1. Partitioning**

**Why it matters?**

- Spark processes data in partitions (small chunks). Poor partitioning can lead to:

   - Too few partitions → underutilized cluster

   - Too many tiny partitions → overhead from task scheduling

   - Uneven partitions → data skew (some nodes do too much work)

**Techniques:**

**✅ Repartition / Coalesce**

```.repartition(n)``` creates equal-sized partitions (can increase or decrease partition count).

```.coalesce(n)``` reduces partitions without full shuffle (efficient when decreasing partition count).

**✅ Partition by relevant keys**

- Partitioning your data on frequently filtered or joined columns can reduce shuffle operations and speed up jobs.

`df.write.partitionBy("country").parquet("/path/to/output")`

**🔹 2. Caching / Persisting**

**Why it matters:**

- If you're reusing the same dataset multiple times (e.g., for joins, aggregations), Spark recomputes it each time unless you cache or persist it.

**Techniques:**

✅ .cache()

- Stores data in memory. Use when data fits in RAM and is reused.

✅ .persist(StorageLevel.DISK_ONLY)

- Stores data on disk if memory is limited.

✅ When to use:

- Reused in multiple actions

- Data is expensive to compute

- You’ve confirmed it fits into memory

**Example:**
```python
df = spark.read.parquet("/data")
df.cache()
result1 = df.filter("year = 2022").count()
result2 = df.filter("country = 'US'").show()
```
**Note:** Without caching, Spark would re-read and re-process /data twice.

**🔹 3. Broadcast Joins**

**Why it matters:**

- If you're joining a large dataset with a small one, Spark normally shuffles both — which is slow and costly.

- Instead, you can broadcast the small one to all executors, avoiding shuffle.

**Techniques:**

✅ Use broadcast() 
```python 
from pyspark.sql.functions
from pyspark.sql.functions import broadcast

large_df = spark.read.parquet("big_table")
small_df = spark.read.csv("lookup_table")

joined = large_df.join(broadcast(small_df), "id")
```

✅ When to use:

- Small dataset fits in memory on each executor (~<10MB, depending on your cluster)

- Join key is well-distributed

**🔹 4. Avoid Wide Transformations**

**Why it matters:**

- Wide transformations (like groupBy(), join(), distinct()) require shuffles — expensive operations that move data between nodes.

- Narrow transformations (like map(), filter()) don’t shuffle data — much faster.

**Optimization Tip:**

- Whenever possible, do more work with narrow operations before triggering a wide transformation.

**Example:**
```python
#Instead of:

df.groupBy("category").count().filter("category != 'unknown'")


#Do:

df.filter("category != 'unknown'").groupBy("category").count()
```


**Note:** Filtering first reduces the amount of data that needs to be shuffled.

**🔹 5. Skew Handling**

**Why it matters:**

- Data skew happens when some keys (like a popular category or user) have much more data than others, causing uneven work distribution and bottlenecks.

**Techniques:**

✅ Salting

- Add random “salt” to the skewed key so data gets distributed across more partitions.
```python
# Example:

from pyspark.sql.functions import rand, concat_ws

df = df.withColumn("join_key_salted", concat_ws("_", df["user_id"], (rand()*10).cast("int")))
```

**Note:**: Do the same salt logic on both sides of the join.

✅ Skew hints (Spark 3+)
```python
df.hint("skew").join(other_df, "user_id")
```

✅ Repartitioning before joins
```Python
df.repartition("user_id").join(other_df, "user_id")
```

**🔹 6. Use DataFrames / Datasets (NOT RDDs)**

**Why it matters:**

- Spark’s Catalyst Optimizer can automatically optimize queries written with DataFrames or SQL, but not RDDs.

✅ Benefits of DataFrames:

- Push down filters

- Reorder joins

- Use column pruning

- Better memory and I/O optimization
```python
#Example:
# Good (DataFrame API)
df.groupBy("category").agg({"price": "avg"})

# Bad (RDD)
rdd.map(lambda x: (x[1], x[2])).reduceByKey(...)
```

**🔹 7. Monitor Spark Jobs (Spark UI)**

**Why it matters:**

- You can't optimize what you can't see.

- Use the Spark Web UI (typically at http://<driver-host>:4040) to analyze:

- Stages and tasks

- Shuffle read/write sizes

- Time spent on garbage collection

- Skewed tasks

- Memory usage

**Look for:**

- Long-running stages

- Large shuffle sizes

- Spilled to disk (indicates memory pressure)

- Uneven task durations (possible skew)

✅ Summary Table
| Technique             | Purpose                                     | Notes                               |
| --------------------- | ------------------------------------------- | ----------------------------------- |
| Partitioning          | Even workload, parallelism                  | Avoid small/huge partitions         |
| Caching/Persisting    | Avoid recomputation of reused data          | Use `.cache()` or `.persist()`      |
| Broadcast Joins       | Avoid shuffle when joining with small table | Use `broadcast()`                   |
| Avoid Wide Transforms | Reduce shuffle and improve speed            | Prefer filter/map over groupBy/join |
| Skew Handling         | Distribute data evenly                      | Use salting, repartitioning         |
| Use DataFrames        | Leverage Catalyst optimizer                 | Avoid RDDs                          |
| Monitor Jobs          | Identify bottlenecks                        | Use Spark UI, logs                  |


## Which one good and Why? Let’s break it down:

| Feature              | **RDD**                          | **DataFrame**                          |
| -------------------- | -------------------------------- | -------------------------------------- |
| **Ease of Use**      | Low-level, more code             | High-level API, easier syntax          |
| **Performance**      | No optimizations                 | Optimized via Catalyst & Tungsten      |
| **Schema**           | No schema (just raw objects)     | Schema-aware (columns, types)          |
| **Optimization**     | Manual tuning needed             | Auto-optimized (query planner)         |
| **Interoperability** | Limited to core Spark APIs       | Works well with Spark SQL, MLlib, etc. |
| **Use Case Fit**     | Complex logic, custom processing | Structured data, analytics, ETL        |

Note: Catalyst manage query execution plan in beeter way to optimise the latency And Tungsten improve memory improvement and execution.

### ✅ Advantages of DataFrames

**🔸 Performance Optimization**

- Spark DataFrames use:

    - Catalyst Optimizer – optimizes query plans (like SQL engines)

    - Tungsten Engine – improves memory management and execution

    - These make DataFrames faster and more efficient than RDDs.

**🔸 Less Code**

- DataFrames are declarative (like SQL). You say what you want, not how to do it.
``` python
#Example:

df.filter(df["age"] > 25).select("name").show()


#vs

rdd.filter(lambda x: x.age > 25).map(lambda x: x.name).collect()
```

**🔸 Integration with SQL & BI Tools**

- You can register DataFrames as temporary views and run SQL queries.

```python
df.createOrReplaceTempView("people")
spark.sql("SELECT name FROM people WHERE age > 25").show()
```

**🔸 Schema Awareness**

- You can inspect and validate data types, which helps with debugging and integration.

## ✅ When to Use RDDs

**Use RDDs only when:**

- You need fine-grained control over data and transformations.

- Your data is unstructured and doesn’t fit well into rows/columns.

- You’re doing low-level transformations or working with custom objects.

- You’re building a custom algorithm that’s hard to express in DataFrame operations.

**🚀 Real-World Recommendation:**

- Start with DataFrames for all ETL, analytics, and machine learning pipelines.

- Drop down to RDDs only if you hit a limitation.

## 🔄 Summary Table

| **Criteria**         | **RDD**                                    | **DataFrame**                             |
| ---------------- | ------------------------------------------ | ----------------------------------------- |
| API Level        | Low-level (functional programming)         | High-level (SQL-like)                     |
| Performance      | Slower, no optimization                    | Faster, Catalyst + Tungsten optimizations |
| Use Case         | Complex transformations, unstructured data | Structured data, standard ETL, analytics  |
| Ease of Use      | Verbose, manual                            | Concise, user-friendly                    |
| Preferred for ML | ❌ (old MLlib)                              | ✅ (better with modern ML pipelines)       |

**✅ Verdict:**

Use DataFrames by default.
Fall back to RDDs only if needed for custom, low-level tasks.


## 🧠 Summary Table
| Memory Type          | Used By        | Purpose                                     |
| -------------------- | -------------- | ------------------------------------------- |
| **Driver Memory**    | Driver Program | Scheduling, job tracking, result collection |
| **Execution Memory** | Executors      | Data processing (joins, shuffles, caching)  |
| **Storage Memory**   | Executors      | Cached RDDs, broadcast variables            |
| **User Memory**      | Executors      | Internal bookkeeping                        |


## ✅ Best Practices

- Avoid ```.collect()``` on large datasets, which can overwhelm driver memory.

- Monitor memory usage using the Spark UI.

- Tune ```spark.driver.memory``` and ```spark.executor.memory``` based on workload size.

- Consider using ```.persist()``` with proper storage levels to optimize memory use.



# What Are ...?
- 1️⃣ Data Integration
- 2️⃣ Data Reconciliation
- 3️⃣ Data Quality Checks
- 4️⃣ Other Related Processes (like Validation, Cleansing, Governance, etc.)

# 🧩 1️⃣ What Is Data Integration

## Definition:

Data Integration is the process of combining data from multiple sources (databases, APIs, flat files, SAP, CRM systems, etc.) into a single, consistent view for analysis, reporting, or downstream use.

🔹 Example:

You may have:

Customer data in SAP

Product data in PostgreSQL

Sales data in BigQuery

Data Integration brings all of these together into a unified data warehouse or data lake, so users can see “Customer → Product → Sales” in one table.

### ⚙️ Typical Steps in Data Integration:
|Step	|Description|
|-------|-----------|
|Extraction|	Get data from source systems (databases, APIs, flat files, etc.)|
|Transformation|	Clean, format, and standardize the data (e.g., date formats, currency conversions)|
|Loading|	Load data into the target system (like BigQuery, Snowflake, etc.)|
|Merging|	Join and relate different datasets (customer IDs, transaction keys, etc.)|
|Consolidation|	Create a single source of truth (Data Warehouse, Data Mart, etc.)


### Source of Truth (Single Source of Truth - SSOT)

A **single source of truth** is a centralized repository or system that serves as the authoritative reference point for all data within an organization. 

### Key Characteristics:

- **Centralized**: All data is stored in one unified location (Data Warehouse, Data Mart, etc.)
- **Authoritative**: It is the official, most up-to-date version of data that all systems reference
- **Eliminates Redundancy**: Prevents data duplication across multiple systems
- **Consistency**: Ensures all stakeholders work with the same, consistent data
- **Reduces Conflicts**: Minimizes discrepancies that arise from inconsistent data across different sources

### In the Context of Consolidation:

During consolidation efforts, disparate data sources are merged into a single, unified system (like a Data Warehouse or Data Mart) to create this SSOT. This ensures that business intelligence, analytics, and reporting are based on consistent, reliable information rather than conflicting versions of the same data.

### Example:
Instead of having customer data scattered across sales, marketing, and support systems, a SSOT would consolidate all customer information into one centralized database that all departments reference.

💡 Tools used: Informatica, Apache NiFi, Talend, Airflow + Python scripts, DBT, etc.

✅ Goal: Provide complete and consistent data to the business, regardless of how many systems exist.

# ⚖️ 2️⃣ What Is Data Reconciliation

Definition:

Data Reconciliation is the process of comparing data between source and target systems to ensure accuracy, completeness, and consistency after integration or migration.

It’s basically a “sanity check” to make sure that data loaded into BigQuery = data extracted from SAP.

🔍 Example:

After loading data from SAP → BigQuery:

|Check Type|	Example|
|---------|---------|
|Count Check|	Source has 10,000 rows → Target should have 10,000 rows
|Sum Check|	Total invoice amount = ₹10M in SAP → should be ₹10M in BigQuery
|Record Matching|	Each invoice_id in SAP exists in BigQuery
|Null Check|	Fields like customer_id should not become null in target
|Duplicate Check|	No extra or missing duplicates in target

✅ Goal: Ensure no data loss, no corruption, no mismatch during ETL.

# 🧹 3️⃣ What Is Data Quality Check

Definition:

Data Quality Checks ensure the data itself is correct, complete, consistent, and reliable for business use.

Even if data successfully moves from SAP → BigQuery, it could still be wrong (like invalid email, future date of birth, negative quantity, etc.).
That’s where Data Quality comes in.


⚙️ Common Data Quality Dimensions:

| Dimension | Meaning | Example Check |
|-----------|---------|----------------|
| Completeness | No missing or null data | All customer IDs should be present |
| Accuracy | Data matches real-world truth | Salary can't be negative |
| Consistency | Same data should match across systems | Gender = "M/F" in all datasets |
| Uniqueness | No duplicate records | Each invoice_id is unique |
| Timeliness | Data is up to date | Last update < 24 hours ago |
| Integrity | Relationships are valid | All foreign keys exist (customer_id → customers table) |
| Validity | Data follows correct formats/rules | Email pattern valid, date not > today |

✅ Goal: Deliver trustworthy data for analysis and reporting.

🧪 Example Data Quality Checks in BigQuery:
- Completeness Check

```sql
SELECT COUNT(*) 
FROM sales 
WHERE customer_id IS NULL;
```


- Uniqueness Check

```sql
SELECT customer_id, COUNT(*) 
FROM customers 
GROUP BY customer_id 
HAVING COUNT(*) > 1;
```
- Integrity Check

```sql
SELECT s.customer_id 
FROM sales s 
LEFT JOIN customers c ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

- Validity Check

```sql
SELECT * FROM customers WHERE email NOT LIKE '%@%.%' OR age > 120;
```

- Timeliness Check

```sql
SELECT COUNT(*) 
FROM sales 
WHERE last_updated < CURRENT_DATE() - 1;
```

# 🧠 4️⃣ Other Related Concepts (Beyond Integration, Reconciliation & Quality)
| Concept	| Description |
|---------|-------------|
Data Validation |	Checking data type, format, and value ranges during ingestion.
Data Cleansing |	Fixing or removing incorrect or inconsistent data (e.g., trimming spaces, correcting spelling).
Data Standardization|Enforcing consistent formats — date (YYYY-MM-DD), currency (USD/INR), etc.
Data Governance |	Policies and processes ensuring data ownership, access control, and compliance (GDPR, HIPAA).
Data Lineage	| Tracking where data came from, how it was transformed, and where it goes (useful for debugging ETL).
Master Data Management (MDM)	| Ensures one consistent version of key entities like “Customer,” “Product,” “Vendor.”
Metadata Management	| Keeping info about data — schema, definitions, owners, last updated, etc.

```
┌─────────────────────────────┐
│ Source Systems (SAP)        │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Data Integration (ETL)      │
│ Extract + Transform + Load  │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Data Reconciliation         │
│ Compare source vs target    │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Data Quality Checks         │
│ Accuracy, completeness      │
└────────────┬────────────────┘
             ↓
┌─────────────────────────────┐
│ Clean, Trusted Data         │
│ Analytics/ML/BI             │
└─────────────────────────────┘
```

Or as a compact diagram:

```
SAP → ETL → Reconciliation → Quality Checks → Analytics
```

✅ In Summary
|Process|	Purpose|	Key Benefit
|---------|---------|---------|
|Data Integration|	Combine multiple data sources	|Unified view of data
|Data Reconciliation|	Verify source = target	|Ensure no data loss or mismatch
|Data Quality Checks|	Verify data correctness	|Ensure reliability and trust
|Data Validation / Cleansing|	Fix and standardize data	|Improve usability
|Data Governance|	Control access and compliance	|Maintain integrity and traceability
|MDM / Lineage|	Manage master entities & flow	|Consistency and transparency