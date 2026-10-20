# ablekimov-alisher-devops

DevOps laboratory work 1: Linux, Git, GitHub, Docker and Jenkins.

- Student: Alisher Ablekimov
- Group: IT2-2312
- Student ID: 37637
- Course: DevOps

## Project structure

```text
app/                 Python application that prints student information
tests/               unit tests for the application
scripts/             Bash script with system information
config/              application settings
logs/                log files (ignored by Git)
backup/              local backups (ignored by Git)
Dockerfile           how the Docker image is built
docker-compose.yml   starts the application with Docker Compose
Jenkinsfile          Jenkins pipeline: Checkout, Build, Test, Docker Build, Docker Run
```
