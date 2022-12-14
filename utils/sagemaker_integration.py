import subprocess
import os
from from_root import from_root
import boto3
import mlflow.sagemaker as mfs
import json

def upload(s3_bucket_name = None, mlruns_direc= None) # s3 bucket name, mlruns_directory
    try:
        output = subprocess.run(["aws", "s3", "sync", "{}".format(mlruns_direc),
                                 "s3://{}".format(s3_bucket_name)],
                                 stdout= subprocess.PIPE,
                                 encoding="utf-8")
        print("\Saved to bucket: ", s3_bucket_name)
        return f"Done uploading: {output.stdout}"

    except Exception as e:
        return f"Error occurred while uploading: {e.__str__()}"