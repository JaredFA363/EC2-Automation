output "instance_public_ip" {
    value = aws_instance.web.public_ip
    description = "Public IP of the EC2 instance"
}

output "healthcheck_url" {
    value = "http://${aws_instance.web.public_ip}/health"
    description = "/health endpoint URL"
}