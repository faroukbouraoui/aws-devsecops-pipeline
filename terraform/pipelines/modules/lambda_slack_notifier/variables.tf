variable "function_name" {
  type        = string
  description = "Nom de la Lambda Slack notifier"
}

variable "slack_webhook_url" {
  type        = string
  sensitive   = true
  description = "Webhook Slack"

}

variable "sns_topic_arn" {
  type        = string
  description = "ARN du topic SNS vers lequel on s'abonne"
}