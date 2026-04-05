# Welcome to Airflow

## Prerequisites
- Docker container for running airflow on docker.
- Essential docker and docker composer commands.
- GCP service account to interact with GCP services.


## 🧩 1️⃣ Apache Airflow Architecture

Apache Airflow is designed around a modular, distributed architecture — meaning its components can scale independently.

## 🔧Core Components
| Component                         | Description                                                                                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Scheduler**                     | Responsible for scheduling jobs (DAGs). It looks at the DAG definitions, determines which tasks are ready to run, and sends them to the executor. |
| **Executor**                      | Actually runs the tasks — either locally (LocalExecutor), in parallel on multiple machines (CeleryExecutor, KubernetesExecutor, etc.).            |
| **Worker(s)**                     | Execute the task instances assigned by the executor. Each worker runs tasks in isolation (like a Docker container, process, or pod).              |
| **Web Server (UI)**               | Provides a web interface for users to visualize DAGs, monitor progress, retry failed tasks, etc. Usually runs via a Flask web app.                |
| **Metadata Database**             | A relational database (e.g., PostgreSQL/MySQL) used to store metadata — DAGs, task states, logs, variables, connections, etc.                     |
| **DAGs Folder (Code Repository)** | A file system or bucket containing all the DAG Python scripts. The scheduler reads them periodically to detect new or updated workflows.          |

## 🏗️ How They Interact

- You write a DAG (Directed Acyclic Graph) — a Python file defining the workflow and task dependencies.

- The Scheduler scans the DAG folder and decides which tasks are ready.

- It uses the Executor to queue those tasks.

- The Executor assigns them to Workers.

- Each Worker executes the task (for example, running a Spark job or a Python script).

- The task’s state (success/failure/etc.) is recorded in the Metadata Database.

- The Web UI continuously reads from the database and shows the DAG and task statuses.

## How to Run and Up Docker Container and Interact with Airlfow
| **Steps**|**Commands**|**Description**|
|----------|------------|---------------|
|1|`docker compose up -d`|To up and run docker compose in detached mode|
|2|`docker compose ps`|To list all services running and in healthy mode or not|
|3|`docker exec -it IMAGE_NAME [airflow-airflow-apiserver-1] bash`|To interact with airlow cli using bash shell|
|4| `airflow version`|To confirm you airflow version, working on|


## Airflow CLIs
|**airflow cli**| **Description**|
|---------------|----------------|
|`airflow dags list`| List all dags|



## Airflow Commands
| **airflow cli** | **Description**|
|------------------|-------------------|
| `airflow version` | To check airflow version|
| `airflow dags list` | To list all DAGs |



# Airflow Operators

| Service                        | Description                                           | Operator Class Names                                                                                                                                                                                                            |
| ------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Python Programming** | To write python functions | `PythonOperator` |
| **MySQL** | To connect through MySQL database | `MySQLConnector` |
| **EmptyOperator** | Empty as ealier known as DummyOperator, it does not anything, just asign | `EmptyOperator` |
| **ShortCircuitOperator** | ShortCircuitOperator operator used for stop the downstream task with condition satisfied | `ShortCircuitOperator` |
| **BigQuery**                   | Run queries, load/extract tables, copy datasets, jobs | `BigQueryInsertJobOperator`, `BigQueryGetDataOperator`, `BigQueryCheckOperator`, `BigQueryIntervalCheckOperator`, `BigQueryValueCheckOperator`, `BigQueryTableExistenceSensor`, `BigQueryExecuteQueryOperator`                                                  |
| **BigQuery Data Transfer**     | Trigger transfer configs                              | `BigQueryCreateDataTransferOperator`, `BigQueryDeleteDataTransferOperator`, `BigQueryUpdateDataTransferOperator`, `BigQueryRunDataTransferOperator`                                                                             |
| **Bigtable**                   | Table / instance ops                                  | `BigtableCreateInstanceOperator`, `BigtableDeleteInstanceOperator`, `BigtableUpdateClusterOperator`, `BigtableGetDataOperator`                                                                                                  |
| **AlloyDB**                    | AlloyDB cluster / backup ops                          | `AlloyDBCreateClusterOperator`, `AlloyDBDeleteClusterOperator`, `AlloyDBCreateBackupOperator`                                                                                                                                   |
| **AutoML**                     | Train / deploy models                                 | `AutoMLTrainModelOperator`, `AutoMLDeployModelOperator`, `AutoMLPredictOperator`                                                                                                                                                |
| **Batch**                      | Submit GCP Batch jobs                                 | `CloudBatchSubmitJobOperator`, `CloudBatchDeleteJobOperator`                                                                                                                                                                    |
| **Build (Cloud Build)**        | Build containers, run steps                           | `CloudBuildCreateBuildOperator`, `CloudBuildCancelBuildOperator`                                                                                                                                                                |
| **Composer**                   | Manage Composer envs                                  | `CloudComposerCreateEnvironmentOperator`, `CloudComposerUpdateEnvironmentOperator`, `CloudComposerDeleteEnvironmentOperator`                                                                                                    |
| **Compute Engine**             | Manage VMs, disks                                     | `ComputeEngineStartInstanceOperator`, `ComputeEngineStopInstanceOperator`, `ComputeEngineInsertInstanceOperator`, `ComputeEngineDeleteInstanceOperator`                                                                         |
| **Cloud SQL**                  | Instance / DB / user mgmt                             | `CloudSQLCreateInstanceOperator`, `CloudSQLDeleteInstanceOperator`, `CloudSQLImportInstanceOperator`, `CloudSQLExportInstanceOperator`, `CloudSQLExecuteQueryOperator`                                                          |
| **Cloud Storage (GCS)**        | Buckets, objects                                      | `GCSCreateBucketOperator`, `GCSDeleteBucketOperator`, `GCSListObjectsOperator`, `GCSDeleteObjectsOperator`, `GCSToBigQueryOperator`, `GCSToGCSOperator`                                                                         |
| **Cloud Run**                  | Deploy services, jobs                                 | `CloudRunDeployServiceOperator`, `CloudRunDeleteServiceOperator`, `CloudRunJobCreateOperator`, `CloudRunJobDeleteOperator`                                                                                                      |
| **Cloud Functions**            | Deploy / invoke functions                             | `CloudFunctionDeployFunctionOperator`, `CloudFunctionDeleteFunctionOperator`, `CloudFunctionInvokeFunctionOperator`                                                                                                             |
| **Data Catalog**               | Tag templates, entries                                | `DatacatalogCreateEntryGroupOperator`, `DatacatalogDeleteEntryOperator`, `DatacatalogCreateTagTemplateOperator`, `DatacatalogUpdateTagOperator`                                                                                 |
| **Data Fusion**                | Pipelines, instances                                  | `CloudDataFusionCreatePipelineOperator`, `CloudDataFusionStartPipelineOperator`, `CloudDataFusionStopPipelineOperator`, `CloudDataFusionDeletePipelineOperator`                                                                 |
| **Data Loss Prevention (DLP)** | Inspection, de-identify                               | `CloudDLPCreateInspectTemplateOperator`, `CloudDLPCreateDeidentifyTemplateOperator`, `CloudDLPInspectContentOperator`, `CloudDLPDeidentifyContentOperator`                                                                      |
| **Dataflow**                   | Launch pipelines                                      | `DataflowCreatePythonJobOperator`, `DataflowCreateJavaJobOperator`, `DataflowTemplatedJobStartOperator`, `DataflowStopJobOperator`                                                                                              |
| **Dataplex**                   | Manage lakes / assets                                 | `DataplexCreateLakeOperator`, `DataplexDeleteLakeOperator`, `DataplexCreateAssetOperator`                                                                                                                                       |
| **Dataprep**                   | Run jobs                                              | `DataprepGetJobsForJobGroupOperator`, `DataprepRunJobGroupOperator`                                                                                                                                                             |
| **Dataproc**                   | Cluster / job ops                                     | `DataprocCreateClusterOperator`, `DataprocDeleteClusterOperator`, `DataprocSubmitJobOperator`, `DataprocSubmitPigJobOperator`, `DataprocSubmitHiveJobOperator`, `DataprocSubmitSparkJobOperator`, `DataprocStopClusterOperator` |
| **Dataproc Metastore**         | Service mgmt                                          | `DataprocMetastoreCreateServiceOperator`, `DataprocMetastoreDeleteServiceOperator`, `DataprocMetastoreUpdateServiceOperator`                                                                                                    |
| **Datastore / Firestore**      | CRUD ops                                              | `DatastoreExportEntitiesOperator`, `DatastoreImportEntitiesOperator`, `FirestoreExportDocumentsOperator`, `FirestoreImportDocumentsOperator`                                                                                    |
| **GKE (Kubernetes Engine)**    | Cluster mgmt                                          | `GKECreateClusterOperator`, `GKEDeleteClusterOperator`, `GKEStartPodOperator`                                                                                                                                                   |
| **Life Sciences**              | Submit pipelines                                      | `LifeSciencesRunPipelineOperator`                                                                                                                                                                                               |
| **Logging**                    | Create sinks, log exports                             | `GcsBucketCreateSinkOperator`, `LoggingExportToGCSOperator`                                                                                                                                                                     |
| **Memorystore**                | Redis / memcache                                      | `MemcacheCreateInstanceOperator`, `MemcacheUpdateInstanceOperator`, `MemcacheDeleteInstanceOperator`                                                                                                                            |
| **Pub/Sub**                    | Topics, subs, publish                                 | `PubSubCreateTopicOperator`, `PubSubDeleteTopicOperator`, `PubSubCreateSubscriptionOperator`, `PubSubPublishMessageOperator`, `PubSubPullOperator`                                                                              |
| **Spanner**                    | Manage DBs                                            | `SpannerInstanceDatabaseCreateOperator`, `SpannerInstanceDatabaseDeleteOperator`, `SpannerQueryDatabaseInstanceOperator`                                                                                                        |
| **Translate API**              | Translate text                                        | `CloudTranslateTextOperator`, `CloudTranslateDocumentOperator`                                                                                                                                                                  |
| **Speech-to-Text / TTS**       | Speech services                                       | `CloudSpeechToTextRecognizeSpeechOperator`, `CloudTextToSpeechSynthesizeOperator`                                                                                                                                               |
| **Vision**                     | Image / OCR                                           | `CloudVisionAnnotateImageOperator`, `CloudVisionDetectTextOperator`                                                                                                                                                             |
| **Video Intelligence**         | Video analysis                                        | `CloudVideoIntelligenceDetectVideoOperator`                                                                                                                                                                                     |
| **Vertex AI (ML Engine)**      | Models, training, endpoints                           | `CreateCustomTrainingJobOperator`, `CreateAutoMLTrainingJobOperator`, `RunBatchPredictionJobOperator`, `DeleteModelOperator`, `DeployModelOperator`                                                                             |
| **Workflows**                  | Execute workflows                                     | `WorkflowsExecuteWorkflowOperator`, `WorkflowsDeleteWorkflowOperator`                                                                                                                                                           |


# Task Trigger Rule
| Trigger Rule                  | Meaning                  |
| ----------------------------- | ------------------------ |
| `ALL_SUCCESS`                 | All must succeed         |
| `ALL_FAILED`                  | All must fail            |
| `ALL_DONE`                    | All finished (any state) |
| `ONE_SUCCESS`                 | At least one success     |
| `ONE_FAILED`                  | At least one failure     |
| `NONE_FAILED`                 | No failures              |
| `NONE_FAILED_MIN_ONE_SUCCESS` | No failure + one success |
| `NONE_SKIPPED`                | No skipped               |
| `ALWAYS`                      | Always run               |

# Airflow Connections
| Connection Type |airflow commands to create connection | Description |
|-----------------|--------------------------------------------------------------------------------------------------------|-------------|
| Google Cloud | `airflow connections add google_cloud_default --conn-type google_cloud_platform --conn-extra '{"project": "YOUR_PROJECT_ID","key_path": "/Folder/YOUR_KEY_FILE.json"}'`| Connection to GCP services using a service account key file.|
| MySQL | `airflow connections add mysql_default --conn-type mysql --conn-host YOUR_HOST --conn-login YOUR_USERNAME --conn-password YOUR_PASSWORD --conn-port 3306` | Connection to a MySQL database. |
| Postgres | `airflow connections add postgres_default --conn-type postgres --conn-host YOUR_HOST --conn-login YOUR_USERNAME --conn-password YOUR_PASSWORD --conn-port 5432` | Connection to a PostgreSQL database. |
| S3 | `airflow connections add s3_default --conn-type s3 --conn-extra '{"aws_access_key_id": "YOUR_ACCESS_KEY","aws_secret_access_key": "YOUR_SECRET_KEY"}'` | Connection to Amazon S3. |
| FTP | `airflow connections add ftp_default --conn-type ftp --conn-host YOUR_HOST --conn-login YOUR_USERNAME --conn-password YOUR_PASSWORD --conn-port 21` | Connection to an FTP server. |
| HTTP | `airflow connections add http_default --conn-type http --conn-host YOUR_HOST --conn-login YOUR_USERNAME --conn-password YOUR_PASSWORD --conn-port 80` | Connection to an HTTP endpoint. |
