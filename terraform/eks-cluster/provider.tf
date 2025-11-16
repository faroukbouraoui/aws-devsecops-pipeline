provider "aws" {
  region = var.region
}

terraform {
  cloud {
    organization = "farouk"

    workspaces {
      name = "dbs-aws-devsecops-eks-cluster"
    }
  }
}
