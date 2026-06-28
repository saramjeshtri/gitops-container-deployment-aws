# gitops-container-deployment-aws

Containerized REST API deployed on AWS ECS Fargate using a GitOps pipeline. Every push to main automatically builds a new Docker image, pushes it to ECR, and redeploys on ECS.

## Stack

- **Runtime:** Python 3.12 + FastAPI
- **Container:** Docker
- **Registry:** AWS ECR
- **Compute:** AWS ECS Fargate
- **Networking:** VPC, ALB, Security Groups
- **IaC:** Terraform
- **CI/CD:** GitHub Actions

## Architecture
GitHub push

↓

GitHub Actions builds Docker image

↓

Pushes to ECR

↓

ECS Fargate pulls new image and redeploys

↓

Traffic routed via Application Load Balancer

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Health check |
| POST | /notes | Create a note |
| GET | /notes | Get all notes |

## Live API

Base URL: `http://notes-api-alb-2041339904.us-east-1.elb.amazonaws.com`

```bash
# Health check
curl http://notes-api-alb-2041339904.us-east-1.elb.amazonaws.com/health

# Create a note
curl -X POST http://notes-api-alb-2041339904.us-east-1.elb.amazonaws.com/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "note title", "content": "note content"}'

# Get all notes
curl http://notes-api-alb-2041339904.us-east-1.elb.amazonaws.com/notes
```

## Deploy

**Prerequisites:** AWS CLI configured, Terraform installed, Docker installed

```bash
# Clone the repo
git clone https://github.com/saramjeshtri/gitops-container-deployment-aws
cd gitops-container-deployment-aws

# Deploy infrastructure
cd infrastructure
terraform init && terraform apply

# Build and push image
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ecr-url>
docker buildx build --platform linux/amd64 -t <ecr-url>:latest --push .

# After setup, every git push triggers automatic redeployment
```
## Requirements

- AWS CLI configured
- Terraform >= 1.0
- Docker installed