# AWS FastAPI Deployment (Terraform + Docker)

This is a portfolio project I built to practice deploying a containerized application to AWS using Terraform.

The goal of this project was to take a FastAPI backend and deploy it securely on AWS using IaC. Everything is automated via Terraform, and the app runs on ECS Fargate.

## Files

*   **app/main.py**: A simple FastAPI application.
*   **Dockerfile**: Instructions to package the app into a Docker container.
*   **terraform/**: The IaC files. This creates a custom VPC, sets up security groups, configures an Application Load Balancer (ALB), and provisions the ECS cluster to run the Docker image.

## Tech Stack
*   **AWS:** VPC, ECS (Fargate), ECR, ALB, IAM
*   **IaC:** Terraform
*   **Code:** Python (FastAPI), Docker

## Instructions

If you want to deploy this yourself, you'll need AWS CLI configured and Terraform installed.

1.  **Push the image to ECR:**
    Сreate an ECR repository and push the Docker image to it.
    ```bash
    # 1. Login to AWS ECR via docker
    aws ecr get-login-password --region <AWS_REGION> | docker login --username AWS --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com
    
    # 2. Build
    docker build -t fastapi-app .
    
    # 3. Tag the image for ECR
    docker tag fastapi-app:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/fastapi-app:latest
    
    # 4. Push the image
    docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/fastapi-app:latest
    ```

2.  **Deploy with Terraform:**
    Navigate to the terraform folder and run:
    ```bash
    cd terraform
    terraform init
    terraform apply
    ```

3.  Once applied, Terraform will output the link of the Load Balancer.

## Challenges & Learnings

Some of the key challenges I overcame include:

*   **IAM Roles & Permissions:** Initially, my ECS tasks were failing to start due to mixed up roles. I learned how to debug AWS permissions and discovered that Fargate requires specific IAM "Execution Roles" for underlying ECS agent just to pull the Docker image from ECR and send logs to CloudWatch.
*   **VPC Networking & Security:** Getting the Application Load Balancer (in a public subnet) to properly route traffic to the ECS containers (in a private subnet) required careful configuration of Security Groups and Target Groups in Terraform.
