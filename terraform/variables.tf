variable "project_name" {
  description = "Project name prefix for resources"
  type        = string
  default     = "ec2_automation"
}

variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "eu-west-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}