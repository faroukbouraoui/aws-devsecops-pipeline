variable "rule_name" {
  type        = string
  description = "Nom de la règle EventBridge"
}

variable "codebuild_project_name" {
  type        = string
  description = "Nom du projet CodeBuild à surveiller"
}

variable "sns_topic_arn" {
  type        = string
  description = "ARN du topic SNS cible"
}