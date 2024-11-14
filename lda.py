import boto3
import os

def lambda_handler(event, context):
    # Initialize Glue client
    glue_client = boto3.client('glue')

    # Name of the Glue job from environment variable
    glue_job_name = os.environ['GLUE_JOB_NAME']

    try:
        # Start the Glue job
        response = glue_client.start_job_run(JobName=glue_job_name)
        print(f"Started Glue job '{glue_job_name}' with JobRunId: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': f"Glue job '{glue_job_name}' started successfully."
        }
    except Exception as e:
        print(f"Error starting Glue job: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error starting Glue job: {str(e)}"
        }
