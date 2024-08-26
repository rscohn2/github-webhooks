===============
GitHub Webhooks
===============

To deploy the cloud function::

    glcoud functions deploy dnn-pr-commentgcloud functions deploy dnn-pr-comment --runtime python312 --trigger-http --allow-unauthenticated --entry-point github_webhook
xxx
    
