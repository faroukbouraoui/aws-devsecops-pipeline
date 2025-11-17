variable "resource_prefix" {
  type        = string
  description = "Prefix for AWS Resources"
  default     = "aws"
}

variable "eks_cluster_name" {
  type        = string
  description = "Name of the EKS Cluster"
  default     = "aws-devsecops-cluster"
}

variable "codebuild_project_name" {
  type    = string
  default = "awsome-fastapi-static-analysis-project" # adapte au nom de ton projet CodeBuild
}

variable "region" {
  type        = string
  description = "AWS Region"
  default     = "eu-west-1"
}

variable "SNYK_TOKEN" {}
variable "SNYK_ORG_ID" {}

variable "alert_email" {
  type        = string
  description = "Email à notifier via SNS"
}

variable "slack_webhook_url" {
  type        = string
  sensitive   = true
  description = "Webhook Slack pour recevoir les notificationss"

}