variable "resource_prefix" {
  type        = string
  description = "Prefix for AWS Resources"
  default     = "aws"
}

variable "region" {
  type        = string
  description = "AWS Region"
  default     = "eu-west-1"
}
