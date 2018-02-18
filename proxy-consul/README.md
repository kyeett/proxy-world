



## Minimal example of 


Start standalone consul-template for testing
$PWD should be a clone of https://github.com/avthart/docker-consul-template
then /examples
```
docker run -v $PWD/:/tmp/ --entrypoint=bash -it avthart/consul-template
```

Add new service
```
curl -X PUT -d '{"Datacenter": "dc1", "Node": "google", "Address": "www.google.com", "Service": {"Service": "search", "Port": 80}}' http://127.0.0.1:8500/v1/catalog/register
```

**Template command**
```
consul-template -consul-addr=192.168.0.10:8500 -template nginx.ctml:here.txt --verbose
``

## This is pretty sick, if it works
[link](https://github.com/hashicorp/consul-template)
Render multiple templates in the same process. The optional third argument to the template is a command that will execute each time the template changes.
```bash
$ consul-template \
    -template "/tmp/nginx.ctmpl:/var/nginx/nginx.conf:nginx -s reload" \
    -template "/tmp/redis.ctmpl:/var/redis/redis.conf:service redis restart" \
    -template "/tmp/haproxy.ctmpl:/var/haproxy/haproxy.conf"
```