from slack_sdk.webhook import WebhookClient
url = ""
webhook = WebhookClient(url)

response = webhook.send(
    blocks=[
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "_______________________________________________________"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": " *Login:*\n passed: 10, failed: 1"
            }
        },
{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "A very important thcfgvhbjning has occurred! <https://alert-system.com/alerts/1234|Click here> for details!"
            }
        }
    ]
)

assert response.status_code == 200
assert response.body == "ok"