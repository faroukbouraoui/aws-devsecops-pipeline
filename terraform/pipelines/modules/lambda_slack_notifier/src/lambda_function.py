import json
import os
import urllib.request
import urllib.error


def lambda_handler(event, context):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("No SLACK_WEBHOOK_URL set in environment variables")
        return

    # Log brut pour debug
    try:
        print("Event received:", json.dumps(event))
    except TypeError:
        print("Event received (non-serializable):", str(event))

    # Si l'event vient de SNS (cas réel CodeBuild -> EventBridge -> SNS)
    records = event.get("Records") if isinstance(event, dict) else None
    if records:
        for record in records:
            sns_msg = record.get("Sns", {}).get("Message", "{}")
            try:
                msg = json.loads(sns_msg)
            except json.JSONDecodeError:
                msg = {}

            detail = msg.get("detail", {})
            project  = detail.get("project-name", "unknown-project")
            build_id = detail.get("build-id", "unknown-build")
            status   = detail.get("build-status", "FAILED")

            text = f"🚨 CodeBuild *{status}* pour le projet *{project}*.\nBuild ID: `{build_id}`"
            send_to_slack(webhook_url, text)
    else:
        # Cas test manuel depuis la console Lambda
        text = f"🧪 Test Lambda reçu : ```{json.dumps(event)}```"
        send_to_slack(webhook_url, text)


def send_to_slack(webhook_url, text):
    data = {"text": text}
    body = json.dumps(data).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=body,
        headers={"Content-Type": "application/json"},
    )

    try:
        with urllib.request.urlopen(req) as resp:
            resp_body = resp.read().decode("utf-8")
            print("Slack response:", resp.status, resp_body)
    except urllib.error.HTTPError as e:
        print("HTTPError when calling Slack:", e.code, e.reason, e.read().decode("utf-8"))
    except urllib.error.URLError as e:
        print("URLError when calling Slack:", e.reason)
    except Exception as e:
        print("Unexpected error when calling Slack:", str(e))