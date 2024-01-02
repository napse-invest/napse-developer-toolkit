mkdir -p provisionEB
touch provisionEB/Dockerrun.aws.json
touch provisionEB/config.json

cp backend/docker/production.yml provisionEB/docker-compose.yml

cat << EOF > provisionEB/Dockerrun.aws.json
{
    "AWSEBDockerrunVersion": "3",
    "Authentication": {
      "bucket": "$AWS_BUCKET_NAME_BACKEND",
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
SECRET_KEY="" # TODO : Generate random password
DJANGO_DEBUG=False
IS_LOCAL=False

# Flower
# ------------------------------------------------------------------------------
CELERY_FLOWER_USER="" # TODO : Generate random password
CELERY_FLOWER_PASSWORD="" # TODO : Generate random password
DB_ENGINE="POSTGRES"
EOF

cat << EOF > backend/.envs/.production/.litestream
DB_SETUP=litestream
LITESTREAM_ACCESS_KEY_ID="" # TODO : Generate random password
LITESTREAM_SECRET_ACCESS_KEY="" # TODO : Generate random password
S3_BUCKET_PATH="${S3_BUCKET_PATH}" # TODO : Create s3 bucket
EOF

mkdir -p provisionEB/.env
mkdir -p provisionEB/.ebextensions
cp backend/.envs/.production/.django provisionEB/.env/.django
cp backend/.envs/.production/.litestream provisionEB/.env/.litestream
# cp backend/.ebextensions/* provisionEB/.ebextensions/ # TODO : Add ebextensions
