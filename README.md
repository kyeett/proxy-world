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

docker run  -p 80:80 --rm --name world-proxy \
            -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
            -v /var/run/docker.sock:/tmp/docker.sock:ro \
            nginx


### Todos
1. Proxy port on ngnix to another service
2. Use consul for service discovery [link](https://github.com/hashicorp/consul-template/blob/master/examples/nginx.md). [competitor?](https://github.com/avthart/docker-consul-template/blob/master/examples/examples.md)
3. Reload consul data [link](https://serverfault.com/questions/378581/nginx-config-reload-without-downtime)

### Dones
1. ~~Simple redirect to google~~
3. ~~Plantuml for system~~
5. ~~Create github repo~~
2. ~~Load balancing between two services~~
4. ~~Docker-compose to start system~~
5. ~~Path-proxy~~

## References
[Using env variables in nginx conf](https://docs.docker.com/samples/library/nginx/)
[online PlantUML editor](https://www.planttext.com/)
