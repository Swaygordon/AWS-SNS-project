import json
import boto3 # type: ignore

sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # Parse the S3 event
    records = event.get('Records', [])
    for record in records:
        s3_bucket = record['s3']['bucket']['name']
        s3_object = record['s3']['object']['key']
        
        message = f"Change detected in S3 bucket: {s3_bucket}\nObject: {s3_object}"
        
        # Send notification
        sns_client.publish(
            TopicArn='arn:aws:sns:<region>:<account-id>:s3-change-alert',
            Message=message,
            Subject="S3 Bucket Change Alert"
        )

    return {"statusCode": 200, "body": "Notification sent successfully"}
