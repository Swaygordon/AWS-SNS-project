                                                  S3, LAMBDA, and SNS NOTIFICATION PROJECT


This project demonstrates how to set up an AWS-based solution to monitor changes in an S3 bucket and notify users via email using AWS services. The system leverages the following AWS components:

Amazon S3: To store objects and detect changes (e.g., uploads, deletions).
AWS Lambda: To process S3 events and trigger actions.
Amazon SNS: To send email notifications to subscribed users.
With this setup, you can automate monitoring of S3 bucket activities and ensure users are promptly informed of any changes. Follow the step-by-step instructions below to implement the solution.

**NOTE**- There's a sample of a python code within the repository.


Here's a step-by-step guide to implement a project that integrates Amazon S3, AWS Lambda, and Amazon SNS to send an email notification when changes occur in an S3 bucket.

1. Create an S3 Bucket

-Log in to AWS Management Console.

-Navigate to the S3 service.

-Click Create bucket.

-Enter a unique bucket name (e.g., my-s3-notification-bucket).

-Choose the region where you want to create the bucket.

-Keep default settings or configure as needed, such as enabling versioning.

-Click Create bucket.



2. Create an SNS Topic

-Navigate to the SNS service in the AWS Console.

-Click Topics > Create topic.

-Select Standard for the topic type.

-Enter a name for the topic (e.g., s3-change-alert).

-Click Create topic.

-After creation, click the topic name to open its details page.

-Create a subscription:

-Click Create subscription.

-Choose the topic ARN from the dropdown.

-Select Protocol as Email.

-Enter the email address to receive notifications.

-Click Create subscription.

-Confirm the subscription:

-Check your email for a confirmation message.

-Click the confirmation link in the email.


3. Create a Lambda Function

-Navigate to the Lambda service.

-Click Create function.

-Select Author from scratch.

-Enter a function name (e.g., S3ChangeHandler).

-Select Runtime as Python 3.x (or your preferred language).

-Under Permissions:

  -Select Change default execution role.
  -Choose Create a new role with basic Lambda permissions.

-Click Create function.

-test function.

-Replace <region> and <account-id> in the TopicArn with your AWS region and account ID.

-Click Deploy to save the function.



4. Add S3 Trigger for Lambda

-In the Lambda function details page, go to the Function overview section.

-Click Add trigger.

-Select S3 as the trigger source.

-Configure the trigger:

-Choose your S3 bucket.

-Select event types (e.g., All object create events or All object delete events).

-Enable the trigger by checking the box.

-Click Add.




5. Set Up Permissions

-Open the IAM Roles section in the AWS Console.

-Find the role associated with your Lambda function.

-Attach the following permissions:
  -AWSLambdaBasicExecutionRole (automatically added during Lambda creation).
  -AmazonSNSFullAccess.
  -AmazonS3ReadOnlyAccess.
-Save the role updates.



6. Test the Setup

-Upload or delete an object in the S3 bucket to trigger the Lambda function.

-Check your email for an alert from SNS.