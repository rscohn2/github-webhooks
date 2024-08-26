import base64
import json
from google.cloud import pubsub_v1

PROJECT_ID = 'uxl-github-webhooks'
TOPIC_ID = 'dnn-pr-comment'

def github_webhook(request):
    request_json = request.get_json()
    print(f"Request JSON: {request_json}")
    
    if 'comment' in request_json:
        comment = request_json['comment']['body']
        publish_to_pubsub(comment)
        return 'Comment published to Pub/Sub', 200
    else:
        return 'No comment found', 400

def publish_to_pubsub(message):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)
    
    message_bytes = message.encode('utf-8')
    publisher.publish(topic_path, data=message_bytes)