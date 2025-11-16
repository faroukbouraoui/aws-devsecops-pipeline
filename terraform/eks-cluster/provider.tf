provider "aws" {
  region = var.region
}

terraform {
  cloud {
    organization = "farouk"

    workspaces {
      name = "dsb-aws-devsecops-eks-cluster"
    }
  }
}
