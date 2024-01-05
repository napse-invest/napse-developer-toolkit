mkdir -p provisionEB
touch provisionEB/Dockerrun.aws.json
touch provisionEB/config.json

cp backend/docker/production.yml provisionEB/docker-compose.yml

cat << EOF > provisionEB/Dockerrun.aws.json
{
    "AWSEBDockerrunVersion": "3",
    "Authentication": {
      "bucket": napse-eb-bucket,
      "key": "config.json"
    }
}
EOF

cat << EOF > provisionEB/config.json
{
    "auths": {
        "ghcr.io": {
            "auth": "$NAPSE_SECRET_DEPLOYMENT_TOKEN_AWS"
        }
    }
}
EOF
mkdir -p backend/.envs
mkdir -p backend/.envs/.production


cat << EOF > backend/.envs/.production/.django
# General secrets
# ------------------------------------------------------------------------------
USE_DOCKER="yes"
IPYTHONDIR="/app/.ipython"

# Redis
# ------------------------------------------------------------------------------
REDIS_URL="redis://redis:6379/0"

# Django
# ------------------------------------------------------------------------------
DJANGO_DEBUG=False
IS_LOCAL=False

# To fill in in JS
# ------------------------------------------------------------------------------
# DJANGO_SECRET_KEY="" # TODO : Generate random password
EOF

cat << EOF > backend/.envs/.production/.litestream
# General secrets
# ------------------------------------------------------------------------------
DB_SETUP="litestream"
DB_ENGINE="SQLITE"

# To fill in in JS
# ------------------------------------------------------------------------------
# AWS_ACCESS_KEY_ID="" # TODO : Get IAM credentials
# AWS_SECRET_ACCESS_KEY="" # TODO : Get IAM credentials
# AWS_S3_BUCKET_URI="" # TODO : Get s3 bucket path

EOF

mkdir -p provisionEB/.env
mkdir -p provisionEB/.ebextensions
cp backend/.envs/.production/.django provisionEB/.env/.django
cp backend/.envs/.production/.litestream provisionEB/.env/.litestream
cp backend/deploy/aws/.ebextensions/* provisionEB/.ebextensions/ 
