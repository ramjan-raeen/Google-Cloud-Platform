# Google Cloud Storage
## ⚙️ Setup and Authentication
| Command                                  | Description                                    |
| ---------------------------------------- | ---------------------------------------------- |
| `gcloud auth login`                      | Log in to your Google Cloud account.           |
| `gcloud config set project <PROJECT_ID>` | Set the active project.                        |
| `gsutil version -l`                      | Check gsutil version and installation details. |
| `gsutil help`                            | Show help and all available commands.          |

## 🪣 Bucket Operations
| Command                                                         | Description                                                               |
| --------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `gsutil mb gs://<BUCKET_NAME>`                                  | Create a new bucket.                                                      |
| `gsutil mb -l <LOCATION> -c <STORAGE_CLASS> gs://<BUCKET_NAME>` | Create bucket with region and class (e.g., `-l asia-south1 -c STANDARD`). |
| `gsutil ls`                                                     | List all buckets in the project.                                          |
| `gsutil ls gs://<BUCKET_NAME>`                                  | List contents of a specific bucket.                                       |
| `gsutil ls -r gs://<BUCKET_NAME>`                               | List all files recursively.                                               |
| `gsutil rb gs://<BUCKET_NAME>`                                  | Remove an empty bucket.                                                   |
| `gsutil rb -f gs://<BUCKET_NAME>`                               | Force remove bucket (even if not empty).                                  |

## 📁 Object/File Operations
| Command                                                | Description                     |
| ------------------------------------------------------ | ------------------------------- |
| `gsutil cp <LOCAL_FILE> gs://<BUCKET_NAME>`            | Upload a file.                  |
| `gsutil cp -r <LOCAL_DIR> gs://<BUCKET_NAME>`          | Upload a directory recursively. |
| `gsutil cp gs://<BUCKET_NAME>/<OBJECT> <LOCAL_PATH>`   | Download a file.                |
| `gsutil cp -r gs://<BUCKET_NAME>/<FOLDER> <LOCAL_DIR>` | Download folder recursively.    |
| `gsutil mv gs://<SRC_PATH> gs://<DEST_PATH>`           | Move or rename files.           |
| `gsutil rm gs://<BUCKET_NAME>/<OBJECT>`                | Delete a file.                  |
| `gsutil rm -r gs://<BUCKET_NAME>/<FOLDER>`             | Delete folder recursively.      |
| `gsutil cat gs://<BUCKET_NAME>/<OBJECT>`               | Display file content.           |

## 🔐 Access Control & Permissions
| Command                                                          | Description                                    |
| ---------------------------------------------------------------- | ---------------------------------------------- |
| `gsutil iam get gs://<BUCKET_NAME>`                              | Get IAM policy for a bucket.                   |
| `gsutil iam set policy.json gs://<BUCKET_NAME>`                  | Apply IAM policy from a file.                  |
| `gsutil acl get gs://<BUCKET_NAME>`                              | Get ACL for a bucket.                          |
| `gsutil acl set private gs://<BUCKET_NAME>`                      | Make bucket private.                           |
| `gsutil acl set public-read gs://<BUCKET_NAME>`                  | Make bucket publicly readable.                 |
| `gsutil defacl set public-read gs://<BUCKET_NAME>`               | Set default ACL for all new objects.           |
| `gsutil signurl -d 1h <PRIVATE_KEY>.json gs://<BUCKET>/<OBJECT>` | Generate signed URL (temporary public access). |

## ⚡ Syncing and Mirroring
| Command                                          | Description                                 |
| ------------------------------------------------ | ------------------------------------------- |
| `gsutil rsync -r <LOCAL_DIR> gs://<BUCKET_NAME>` | Sync local folder → GCS.                    |
| `gsutil rsync -r gs://<BUCKET_NAME> <LOCAL_DIR>` | Sync GCS → local folder.                    |
| `gsutil rsync -d -r <SRC> <DEST>`                | Sync and delete extra files at destination. |

## 📊 Bucket and Object Management
| Command                                                  | Description                           |
| -------------------------------------------------------- | ------------------------------------- |
| `gsutil du -sh gs://<BUCKET_NAME>`                       | Show total size of a bucket.          |
| `gsutil du -h gs://<BUCKET_NAME>/**`                     | Show size of each object.             |
| `gsutil stat gs://<BUCKET_NAME>/<OBJECT>`                | Display metadata about an object.     |
| `gsutil ls -L gs://<BUCKET_NAME>/<OBJECT>`               | Detailed info (size, metadata, etc.). |
| `gsutil cors get gs://<BUCKET_NAME>`                     | Get CORS configuration.               |
| `gsutil cors set cors.json gs://<BUCKET_NAME>`           | Set CORS policy.                      |
| `gsutil lifecycle get gs://<BUCKET_NAME>`                | Get lifecycle rules.                  |
| `gsutil lifecycle set lifecycle.json gs://<BUCKET_NAME>` | Set lifecycle rules.                  |

## 🧰 Advanced Commands
| Command                                                                     | Description                        |
| --------------------------------------------------------------------------- | ---------------------------------- |
| `gsutil rename gs://<BUCKET_NAME>/<OLD_NAME> gs://<BUCKET_NAME>/<NEW_NAME>` | Rename an object.                  |
| `gsutil rewrite -s NEARLINE gs://<BUCKET_NAME>/<OBJECT>`                    | Change storage class of an object. |
| `gsutil notification create -t <TOPIC_NAME> -f json gs://<BUCKET_NAME>`     | Create Pub/Sub notification.       |
| `gsutil notification list gs://<BUCKET_NAME>`                               | List all notifications.            |
| `gsutil notification delete <NOTIFICATION_ID> gs://<BUCKET_NAME>`           | Delete a notification.             |

## 🧹 Cleanup and Maintenance
| Command                              | Description                         |
| ------------------------------------ | ----------------------------------- |
| `gsutil rm -r gs://<BUCKET_NAME>/**` | Delete all objects in a bucket.     |
| `gsutil rb -f gs://<BUCKET_NAME>`    | Delete bucket and all its contents. |
|                                      |                                     |
 -----------------------------------------------------------------------------


# Google Cloud Storage Lifecycle
## 🧠 What is Lifecycle Management?
Lifecycle Management in GCS automates how your objects (files) are stored and deleted over time — based on rules you define.

You can:

Automatically delete old objects.

Automatically change storage class (e.g., from STANDARD → NEARLINE → COLDLINE → ARCHIVE).

Automatically keep only recent versions if object versioning is enabled.

Basically, it helps save cost and manage data retention automatically.

## ⚙️ Lifecycle Policy Structure
Lifecycle management is defined as a JSON configuration file and attached to a bucket using gsutil or the Console.

A policy has:

    . Action: What to do (e.g., delete, set storage class)

    . Condition: When to do it (e.g., after 30 days, when older versions exist, etc.)

## Sample for rule json file
`{
  "rule": [
    {
      "action": {"type": "Delete"},
      "condition": {"age": 30}
    },
    {
      "action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
      "condition": {"age": 15}
    }
  ]
}
`

## ⚡ Supported Actions
| Action            | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| `Delete`          | Permanently deletes objects matching the condition                |
| `SetStorageClass` | Changes the object’s storage class (e.g. to NEARLINE or COLDLINE) |

## 🧩 Supported Conditions
*Note*: You can define multiple conditions (all must be true for a rule to trigger):
| Condition                 | Meaning                                                                       |
| ------------------------- | ----------------------------------------------------------------------------- |
| `age`                     | Object age in **days** since creation                                         |
| `createdBefore`           | Date (YYYY-MM-DD) before which the object was created                         |
| `isLive`                  | `true` → current version, `false` → noncurrent version (requires versioning)  |
| `numNewerVersions`        | Triggers if object has more than this number of newer versions                |
| `matchesStorageClass`     | Apply rule only to certain storage classes                                    |
| `customTimeBefore`        | Based on custom time metadata field (useful for data retention rules)         |
| `daysSinceCustomTime`     | Trigger after N days since custom time                                        |
| `daysSinceNoncurrentTime` | Trigger after N days since an object became noncurrent (used with versioning) |

## 🔧 Applying Lifecycle Rules
`gsutil lifecycle set lifecycle.json gs://my-bucket`

## To see the lifecycle Rules.
`gsutil lifecycle get gs://my-bucket`

## To delete the lifecycle Rule.
First create empty json file, i.e with no rule.

`echo '{}' > empty_gs_rule.json`

`gsutil lifecycle set empty_gs_rule.json gs://my-bucket`

# Object Versioning on GCS

## 🧩 What is Object Versioning?

Object versioning keeps old versions of objects when they are overwritten or deleted.

So instead of losing data when you replace a file, GCS:

    . Keeps the old copy (called a noncurrent version)

    . Stores the new one as the current version

That way, you can recover or permanently delete old versions later.


## ✅ Step 1: Enable Versioning
`gsutil versioning set on my-bucket`

## Verify it's enable
`gsutil versioning get gs://my-bucket`

## Disable Versioning
`gsutil versioning set off gs://my-bucket`


