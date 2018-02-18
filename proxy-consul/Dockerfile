FROM nginx
MAINTAINER Magnus Wahlstrand <magnus.wahlstrand@gmail.com>

ENV CONSUL_TEMPLATE_VERSION 0.18.1

ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS /tmp/
ADD https://releases.hashicorp.com/consul-template/${CONSUL_TEMPLATE_VERSION}/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /tmp/

RUN apt-get update; apt-get install -y zip unzip bash curl

RUN cd /tmp && \
    sha256sum -c consul-template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS 2>&1 | grep OK && \
    unzip consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \
    mv consul-template /bin/consul-template && \
    rm -rf /tmp

#ADD ./example.ctmpl
ADD ./start-nginx-consul-template.sh ./

ENTRYPOINT ["./start-nginx-consul-template.sh"]