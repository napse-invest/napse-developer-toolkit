export GITHUB_AUTH_TOKEN=$(echo "$NAPSE_DEPLOY_USERNAME:$NAPSE_SECRET_DEPLOYMENT_TOKEN_AWS" | tr -d "\n" | base64)
mkdir -p provisionEB
touch provisionEB/Dockerrun.aws.json
touch provisionEB/config.json

cat <<EOF >provisionEB/docker-compose.yml
version: '3'
name: napse-dtk-production

volumes:
  db_volume: {}

services:
  django: &django
    image: ghcr.io/napse-invest/napse-developer-toolkit/napse_dtk_prod_django:$NAPSE_VERSION
    container_name: django
    env_file:
      - ./.envs/.django
      - ./.envs/.litestream
    environment:
      - DJANGO_SECRET_KEY
      - AWS_ACCESS_KEY_ID
      - AWS_SECRET_ACCESS_KEY
      - AWS_S3_BUCKET_URI
      - NAPSE_API_DOMAIN
    platform: linux/x86_64
    depends_on:
      - redis
    command: /start
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.django.rule=Host(\`\$NAPSE_API_DOMAIN\`)"
      - "traefik.http.routers.django.entrypoints=websecure"
      - "traefik.http.routers.django.tls.certresolver=myresolver"
      - "traefik.http.services.django.loadbalancer.server.port=8000"
      
    expose:
      - "8000"
    volumes:
      - db_volume:/app/db
    ulimits:
      core: 
        soft: 0
        hard: 0

  traefik:
    image: "traefik:v2.9.5"
    container_name: traefik
    command:
      - "--log.level=DEBUG"
      - "--api.insecure=true"
      - "--providers.docker=true"
      - "--providers.docker.exposedbydefault=false"
      - "--entrypoints.web.address=:80"
      - "--entrypoints.websecure.address=:443"
      - "--certificatesresolvers.myresolver.acme.httpchallenge=true"
      - "--certificatesresolvers.myresolver.acme.httpchallenge.entrypoint=web"
      - "--certificatesresolvers.myresolver.acme.email=napse.invest@gmail.com"
      - "--certificatesresolvers.myresolver.acme.storage=/letsencrypt/acme.json"
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock:ro"
      - "./letsencrypt:/letsencrypt"

  celeryworker:
    <<: *django
    container_name: celeryworker
    restart: on-failure
    depends_on:
      - redis
      - django
    ports: []
    command: /start-celeryworker
    labels:
      - "traefik.enable=false"

  celerybeat:
    <<: *django
    container_name: celerybeat
    restart: on-failure
    depends_on:
      - redis
      - django
    ports: []
    command: /start-celerybeat
    labels:
      - "traefik.enable=false"

  redis:
    image: redis:6
    container_name: redis
EOF

cat <<EOF >provisionEB/Dockerrun.aws.json
{
    "AWSEBDockerrunVersion": "3",
    "Authentication": {
      "bucket": "napse-eb-bucket",
      "key": "config.json"
    }
}
EOF

cat <<EOF >provisionEB/config.json
{
    "auths": {
        "ghcr.io": {
            "auth": "$GITHUB_AUTH_TOKEN"
        }
    }
}
EOF
mkdir -p backend/.envs
mkdir -p backend/.envs/.production

cat <<EOF >backend/.envs/.production/.django
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
DJANGO_SETTINGS_MODULE="config.settings.production"

# To fill in in JS
# ------------------------------------------------------------------------------
# DJANGO_SECRET_KEY="" # TODO : Generate random password
EOF

cat <<EOF >backend/.envs/.production/.litestream
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

mkdir -p provisionEB/.envs
mkdir -p provisionEB/.ebextensions
cp backend/.envs/.production/.django provisionEB/.envs/.django
cp backend/.envs/.production/.litestream provisionEB/.envs/.litestream
cp -r backend/deploy/aws/.ebextensions/* provisionEB/.ebextensions/
cp -r backend/deploy/aws/.platform/ provisionEB/.platform/
