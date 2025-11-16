import json
import os
import urllib.request

def lambda_handler(event, context):
    webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
    if not webhook_url:
        print("No SLACK_WEBHOOK_URL set")
        return

    print("Event received:", json.dumps(event))

    for record in event.get("Records", []):
        sns_msg = record.get("Sns", {}).get("Message", "{}")
        try:
            msg = json.loads(sns_msg)
        except json.JSONDecodeError:
            msg = {}

        detail = msg.get("detail", {})
        project  = detail.get("project-name", "unknown-project")
        build_id = detail.get("build-id", "unknown-build")
        status   = detail.get("build-status", "FAILED")

        text = f"🚨 CodeBuild *{status}* for project *{project}*.\nBuild ID: `{build_id}`"

        data = {"text": text}

        req = urllib.request.Request(
            webhook_url,
            data=json.dumps(data).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req) as resp:
            print("Slack response:", resp.read().decode("utf-8"))