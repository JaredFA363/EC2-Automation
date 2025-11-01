terraform {
  backend "s3" {
    bucket         = "infra-backend-s3"
    key            = "terraform.tfstate"
    region         = "eu-west-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}