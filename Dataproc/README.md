# Create dataproc cluster

`gcloud dataproc clusters create hands-on-cluster \
--region asia-south1 \
--zone asia-south1-a \
--master-machine-type=e2-standard-4 \
--worker-machine-type=e2-standard-2 \
--num-workers=2 \
--optional-components=JUPYTER \
--enable-gateway-component`

gcloud dataproc clusters list --region asia-south1

gcloud dataproc jobs submit pyspark \                                             
gs://dataproc-staging-asia-south1-550059806476-lgrdqsu4/notebooks/jupyter/demo04.py \
--region asia-south1 \
--cluster hands-on-cluster \
--bucket dataproc-staging-asia-south1-550059806476-lgrdqsu4/stagging

gcloud dataproc jobs list --region asia-south1

gcloud dataproc jobs describe 0d3a92856d744eaba8821e9be8b567f6 --region asia-south1

gcloud dataproc clusters describe hands-on-cluster 

gcloud dataproc clusters update hands-on-cluster \
--num-workers=3 \
--region asia-south1

gcloud dataproc clusters diagnose hands-on-cluster --region asia-south1
