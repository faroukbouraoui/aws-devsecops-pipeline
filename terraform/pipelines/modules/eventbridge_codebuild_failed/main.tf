resource "aws_cloudwatch_event_rule" "this" {
  name        = var.rule_name
  description = "Trigger on CodeBuild FAILED for project ${var.codebuild_project_name}"

  event_pattern = jsonencode({
    "source"      : ["aws.codebuild"],
    "detail-type" : ["CodeBuild Build State Change"],
    "detail" : {
      "build-status" : ["FAILED"],
      "project-name" : [var.codebuild_project_name]
    }
  })
}

resource "aws_cloudwatch_event_target" "sns_target" {
  rule      = aws_cloudwatch_event_rule.this.name
  target_id = "send-to-sns"
  arn       = var.sns_topic_arn
}