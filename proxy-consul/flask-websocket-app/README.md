
```
# Build docker
docker build -t flask-websocket-app .

# Run docker
docker run  --rm \
            -p 5000:5000 \
            -e BASE_URL=http://localhost/ \
            -e FILENAME=/app/nginx.conf \
            flask-websocket-app

```