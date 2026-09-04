output "alb_dns_name" {
  description = "The DNS name of the load balancer"
  value       = aws_lb.fastapi_lb.dns_name
}
