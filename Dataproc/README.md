# What is Dataproc?

Dataproc is a managed service for running Apache Spark and Apache Hadoop clusters in Google Cloud Platform (GCP). It simplifies the process of creating, managing, and scaling big data clusters without the need to manage the underlying infrastructure.
# Prerequisites
- A Google Cloud Platform account with billing enabled.
- The Google Cloud SDK installed on your local machine.
- Basic knowledge of Apache Spark and Hadoop.
# Steps to create and manage a Dataproc cluster
1. **Create a Dataproc Cluster**: Use the `gcloud` command-line tool to create a Dataproc cluster. You can specify the number of nodes, machine types, and other configurations.
2. **Submit Jobs**: Once the cluster is created, you can submit Spark or Hadoop jobs using the `gcloud dataproc jobs submit` command.
3. **Monitor Jobs**: You can monitor the status of your jobs using the `gcloud dataproc jobs list` and `gcloud dataproc jobs describe` commands.
4. **Update Cluster**: You can update the cluster configuration, such as adding or removing worker nodes, using the `gcloud dataproc clusters update` command.
5. **Diagnose Issues**: If you encounter issues with your cluster, you can use the `gcloud dataproc clusters diagnose` command to gather diagnostic information.
## Example Commands      

## Create dataproc cluster

```bash 
gcloud dataproc clusters create hands-on-cluster \
--region=us-central1 \
--zone=us-central1-a \
\
--master-machine-type=e2-standard-4 \
--worker-machine-type=e2-standard-2 \
--num-workers=2 \
\
--network=default \
--subnet=default \
--no-address \
\
--service-account=dataproc-sa@PROJECT_ID.iam.gserviceaccount.com \
--scopes=https://www.googleapis.com/auth/cloud-platform \
\
--image-version=2.1-debian11 \
--optional-components=JUPYTER \
--enable-component-gateway \
\
--properties=\
spark:spark.sql.shuffle.partitions=200,\
spark:spark.executor.memory=4g,\
spark:spark.driver.memory=2g \
\
--max-idle=1h \
--bucket=dataproc-staging-bucket

```
**Arguments explanation:**

- `hands-on-cluster`: The name of the Dataproc cluster to be created.
- `us-central1`: The region where the cluster will be created.
- `us-central1-a`: The zone within the region.

**flags explanation:**
- `--region`: Specifies the region where the cluster will be created.
- `--zone`: Specifies the zone within the region.
- `--master-machine-type`: Specifies the machine type for the master node.
- `--worker-machine-type`: Specifies the machine type for the worker nodes.
- `--num-workers`: Specifies the number of worker nodes in the cluster.
- `--optional-components`: Specifies additional components to be installed on the cluster, such as Jupyter.
- `--network`: Specifies the VPC network for the cluster.
- `--subnet`: Specifies the subnet within the VPC network.
- `--no-address`: Indicates that the cluster nodes will not have external IP addresses.
- `--service-account`: Specifies the service account to be used by the cluster.
- `--scopes`: Specifies the OAuth scopes for the service account.
- `--image-version`: Specifies the Dataproc image version to be used for the cluster.
- `--properties`: Specifies configuration properties for Spark and Hadoop.
- `--max-idle`: Specifies the maximum idle time before the cluster is automatically deleted.
- `--bucket`: Specifies the Cloud Storage bucket for staging files.
- `--enable-gateway-component`: Enables the gateway component for accessing web interfaces like Jupyter.

**What is machine type?**

Machine types define the hardware configuration of virtual machine instances in Google Cloud. They specify the number of virtual CPUs (vCPUs), memory (RAM), and other resources allocated to the instance. Different machine types are optimized for various workloads, such as general-purpose, compute-optimized, memory-optimized, and more. Choosing the right machine type is crucial for balancing performance and cost based on the specific requirements of your applications.

**Basic machine types:**

example: `n1-standard-4`
Part | Meaning
--- | ---
n1 | Machine family (N1 is a general-purpose machine type)
standard | Machine type category (standard indicates a balanced configuration of CPU and memory)
4 | Number of vCPUs (4 vCPUs in this case)

**Standard(N1 Family) machine types:**
- `n1-standard-1`: 1 vCPU, 3.75 GB RAM
- `n1-standard-2`: 2 vCPUs, 7.5 GB RAM
- `n1-standard-4`: 4 vCPUs, 15 GB RAM

**E2 Family machine types:**
- `e2-standard-2`: 2 vCPUs, 8 GB RAM
- `e2-standard-4`: 4 vCPUs, 16 GB RAM
- `e2-highmem-4`: 4 vCPUs, 32 GB RAM
- `e2-highcpu-4`: 4 vCPUs, 4 GB RAM

**N2 Family machine types:**
- `n2-standard-4`: 4 vCPUs, 16 GB RAM
- `n2-highmem-4`: 4 vCPUs, 32 GB RAM

**C2 Family machine types:**
- `c2-standard-4`: 4 vCPUs, 16 GB RAM
- `c2-standard-8`: 8 vCPUs, 32 GB RAM

**M2/M3(Memory-optimized) Family machine types:**
- `m2-ultramem-64`: 64 vCPUs, 1,024 GB RAM
- `m3-megamem-64`: 64 vCPUs, 896 GB RAM

## List clusters
```bash
gcloud dataproc clusters list --region us-central1
```
## Update cluster
````bash
gcloud dataproc clusters update hands-on-cluster \
--region us-central1 \
--num-workers=3
````
## Diagnose cluster
```bash
gcloud dataproc clusters diagnose hands-on-cluster --region us-central1
```
## Describe a cluster
```bash
gcloud dataproc clusters describe hands-on-cluster --region us-central1
```


## Submit a PySpark job
```bash
gcloud dataproc jobs submit pyspark gs://my-bucket/my-script.py \
--region us-central1 \
--cluster hands-on-cluster \
--bucket my-bucket/staging
```

## Submit a Hadoop job
```bash
gcloud dataproc jobs submit hadoop \
--region us-central1 \
--cluster hands-on-cluster \
--class org.apache.hadoop.examples.WordCount \
--jars file:///usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar \
-- gs://my-bucket/input.txt gs://my-bucket/output/
```
## Submit a Spark job
```bash
gcloud dataproc jobs submit spark \
--region us-central1 \
--cluster hands-on-cluster \
--class org.apache.spark.examples.SparkPi \
--jars file:///usr/lib/spark/examples/jars/spark-examples.jar \
-- 1000
```

## Submit a Spark SQL job
```bash
gcloud dataproc jobs submit spark-sql \
--region us-central1 \
--cluster hands-on-cluster \
--execute 'SELECT COUNT(*) FROM my_table'
```
OR 
```bash
gclud dataproc jobs submit spark-sql \
--region us-central1 \
--cluster hands-on-cluster \
--file gs://my-bucket/my-spark-sql-script.sql
```

## Submit a Hive job
```bash
gcloud dataproc jobs submit hive \
--region us-central1 \
--cluster hands-on-cluster \
--execute 'SELECT * FROM my_table LIMIT 10'
```
OR 
```bash
gcloud dataproc jobs submit hive \
--region us-central1 \
--cluster hands-on-cluster \
--file gs://my-bucket/my-hive-script.hql
```

## List jobs
```
gcloud dataproc jobs list --region us-central1
```
## Describe a job
```bash
gcloud dataproc jobs describe JOB_ID --region us-central1
```
## Stop cluster
```bash
gcloud dataproc clusters stop hands-on-cluster --region us-central1
```
## Start cluster
```bash
gcloud dataproc clusters start hands-on-cluster --region us-central1
```
## Delete cluster
```bash
gcloud dataproc clusters delete hands-on-cluster --region us-central1
```
# Cleanup
To avoid incurring unnecessary charges, make sure to delete any Dataproc clusters you no longer need using the `gcloud dataproc clusters delete` command.
# Additional Resources
- [Dataproc Documentation](https://cloud.google.com/dataproc/docs)
- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs)   