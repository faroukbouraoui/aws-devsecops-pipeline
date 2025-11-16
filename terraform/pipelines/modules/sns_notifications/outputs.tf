output "topic_arn" {
  value       = aws_sns_topic.this.arn
  description = "ARN du topic SNS"
}