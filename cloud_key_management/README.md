# How to use KMS (Key Management Service) in GCP to encrypt and decrypt key vault secrets.
KMS (Key Management Service) in Google Cloud Platform (GCP) is a service that allows you to manage cryptographic keys for your cloud services. It provides a secure and convenient way to encrypt and decrypt data, such as secrets stored in a vault. In this guide, we will go through the steps to use KMS to encrypt and decrypt secrets in a vault, ensuring that your sensitive information is protected while at rest and in transit. We will cover how to create KMS keys, manage access to those keys, and use them to encrypt and decrypt secrets in a vault. By following these steps, you can enhance the security of your secrets and ensure that only authorized users and applications can access them.


# How to use KMS (Key Management Service) in GCP to encrypt and decrypt BigQuery table data.
Steps to use KMS:
1. Create a KMS key into GCP 
2. Give Project access to dedicated user to manage the KMS key
3. Create a service account and give it access to the KMS key
4. Create a key ring and a key in the KMS
5. Encrypt the secret using the KMS key
6. Store the encrypted secret in the vault
7. Configure vault to use the KMS key for decryption
8. Use vault to retrieve the decrypted secret when needed
9. Ensure that the vault has the necessary permissions to access the KMS key for decryption
10. Regularly rotate the KMS key and update the vault configuration accordingly to maintain security.

## gcloud commands for KMS

### List Keys

gcloud kms keys list --keyring [KEY_RING_NAME] --location [LOCATION]

### Create Key

gcloud kms keys create [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --purpose encryption

### Delete Key

gcloud kms keys delete [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION]

### Create Key Ring

gcloud kms keyrings create [KEY_RING_NAME] --location [LOCATION]

### Encrypt Data

gcloud kms encrypt --key [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --plaintext-file [PLAINTEXT_FILE] --ciphertext-file [CIPHERTEXT_FILE]

### Decrypt Data

gcloud kms decrypt --key [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --ciphertext-file [CIPHERTEXT_FILE] --plaintext-file [PLAINTEXT_FILE]

### Rotate Key

gcloud kms keys rotate [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION]

### Set IAM Policy

gcloud kms keys add-iam-policy-binding [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --member serviceAccount:[SERVICE_ACCOUNT_EMAIL] --role roles/cloudkms.cryptoKeyEncrypter

### Remove IAM Policy Binding

gcloud kms keys remove-iam-policy-binding [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --member serviceAccount:[SERVICE_ACCOUNT_EMAIL] --role roles/cloudkms.cryptoKeyEncrypter

## Using Service Account for Encryption and Decryption

To use a service account for encryption and decryption with KMS, follow these steps:

1. **Create a Service Account**:
   
gcloud iam service-accounts create [SERVICE_ACCOUNT_NAME] --display-name "[DISPLAY_NAME]"

2. **Grant Permissions**:
   
gcloud kms keys add-iam-policy-binding [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --member serviceAccount:[SERVICE_ACCOUNT_EMAIL] --role roles/cloudkms.cryptoKeyEncrypter

3. **Encrypt Data**:
   Use the service account to encrypt data:
   ```bash
   gcloud kms encrypt --key [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --plaintext-file [PLAINTEXT_FILE] --ciphertext-file [CIPHERTEXT_FILE] --account [SERVICE_ACCOUNT_EMAIL]
   ```

4. **Decrypt Data**:
   Use the service account to decrypt data:
   ```bash
   gcloud kms decrypt --key [KEY_NAME] --keyring [KEY_RING_NAME] --location [LOCATION] --ciphertext-file [CIPHERTEXT_FILE] --plaintext-file [PLAINTEXT_FILE] --account [SERVICE_ACCOUNT_EMAIL]
   ```

### Example
Assuming you have a key named `my-key` in a key ring `my-keyring` located in `us-central1`, and a service account `my-service-account@my-project.iam.gserviceaccount.com`:

- **Encrypting a file**:
   ```bash
   gcloud kms encrypt --key my-key --keyring my-keyring --location us-central1 --plaintext-file my-secret.txt --ciphertext-file my-secret.enc --account my-service-account@my-project.iam.gserviceaccount.com
   ```

- **Decrypting a file**:
   ```bash
   gcloud kms decrypt --key my-key --keyring my-keyring --location us-central1 --ciphertext-file my-secret.enc --plaintext-file my-secret.txt --account my-service-account@my-project.iam.gserviceaccount.com
   ```