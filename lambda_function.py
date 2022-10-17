import requests

def handler(event, context):
    message = "Issue Created: " + event['issue']['html_url']
    requests.post(
                url="blah",
                json={"text": message}
                    )
