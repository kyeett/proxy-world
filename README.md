# Proxy-world

Learning about `ngnix` and proxies, load balancing, etc.

### Target system view
![Overview of the system](system.png)

### Starting system
```bash
docker run  -p 80:80 --rm --name world-proxy \
            -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
            nginx
```

### Todos
1. Proxy port on ngnix to another service
2. Load balancing between two services
4. Docker-compose to start system
5. Path-proxy

### Dones
1. ~~Simple redirect to google~~
3. ~~Plantuml for system~~
5. ~~Create github repo~~

## References
[online PlantUML editor](https://www.planttext.com/)