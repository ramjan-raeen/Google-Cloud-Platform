# README Structure
## 1. Project Overview

- What this project is
- Business scenario
- Architecture
- Learning objectives

## 2. Technology Stack
| Component                  | Purpose                           |
| -------------------------- | --------------------------------- |
| Airflow                    | Workflow Orchestration            |
| CeleryExecutor             | Distributed Task Execution        |
| Redis                      | Celery Broker                     |
| PostgreSQL                 | Airflow Metadata + Data Warehouse |
| MySQL                      | Source OLTP Database              |
| Kafka                      | Streaming Platform                |
| Kafka UI                   | Kafka Monitoring                  |
| Spark Structured Streaming | Stream Processing                 |
| Wikipedia EventStream      | Streaming Data Source             |
| pgAdmin                    | PostgreSQL Administration         |
| Adminer                    | MySQL Administration              |
| Docker Compose             | Infrastructure                    |



## 3. Complete Architecture Diagram
                         +----------------------+
                         |   Wikipedia Events   |
                         +----------+-----------+
                                    |
                                    |
                           Python Producer
                                    |
                                    |
                              Kafka Topic
                                    |
                                    |
                  +-----------------+----------------+
                  |                                  |
          Kafka UI                           Spark Streaming
                                                     |
                                                     |
                                             PostgreSQL Warehouse
                                                     |
                                                     |
                                                 Airflow DAG
                                                     |
                                                     |
                                            BigQuery / GCS

## GCP connection setup:
```bash
airflow connections add google_cloud_default \
    --conn-type google_cloud_platform \
    --conn-extra '{
        "extra__google_cloud_platform__key_path": "/opt/airflow/keys/gcp_key.json",
        "extra__google_cloud_platform__project": "hands-on-dev-202409"
    }'
```