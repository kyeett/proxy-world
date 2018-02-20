# Proxy-world

Learning about `ngnix` and proxies, load balancing, etc.

### Known bugs

### Todo:s
11. Websocket flask app
13. Handle multiple services with same name
14. Count multiple services with same name
12. Run flask app from nginx ([link](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04), [link2](https://github.com/tiangolo/uwsgi-nginx-flask-docker))
13. Handle (or mark) Unhealthy services from consul

### Target system view
![Overview of the system](system.png)

### Starting system
```bash
docker run  -p 80:80 --rm --name world-proxy \
            -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf \
            nginx
```

### Done:s
1. ~~Simple redirect to google~~
3. ~~Plantuml for system~~
5. ~~Create github repo~~
2. ~~Load balancing between two services~~
4. ~~Docker-compose to start system~~
5. ~~Path-proxy~~
2. ~~Use consul for service discovery [link](https://github.com/hashicorp/consul-template/blob/master/examples/nginx.md). [competitor?](https://github.com/avthart/docker-consul-template/blob/master/examples/examples.md)~~
3. ~~Reload consul data [link](https://serverfault.com/questions/378581/nginx-config-reload-without-downtime)~~
10. ~~Update PlantUml for `nginx-consul-template`~~
9. ~~`docker-compose` for `nginx-consul-template`~~
12. ~~Create and push docker for simple web app~~
12. ~~Flask monitor file change~~
13. ~~Make web app pretty~~

### Fixed bugs
1. ~~BUG #1: Infinite redirect from nginx to flask: `localhost redirected you too many times.`. Workaround exists.~~ Fixed with`, strict_slashes=False` ([SO answer](https://stackoverflow.com/questions/21050320/flask-301-response))
2. ~~BUG #2: SocketIO events sent from python thread didn't reach the browser and seems to break the manual sending.~~ Fixed with `socketio.start_background_task` instead of Thread`, and `eventlet.sleep` instead of `time.sleep` and `polling`. ([SO answer](https://stackoverflow.com/questions/43801884/how-to-run-python-socketio-in-thread))


## References
[Using env variables in nginx conf](https://docs.docker.com/samples/library/nginx/)
[online PlantUML editor](https://www.planttext.com/)
[Flask + SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
[SocketIO example python](http://timmyreilly.azurewebsites.net/flask-socketio-and-more/) 
