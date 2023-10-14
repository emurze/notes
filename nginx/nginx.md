# Nginx

### DNS

![ssl_connect](images/dns_explanation.png)

### SLL

![ssl_connect](images/ssl_connect.png)

![ssl_connect_2](images/ssl_connect_2.png)

![certbot](images/certbot.png)

### A/B Testing

![ab_testing](images/ab_testing.png)

![ab_testing_2](images/ab_testing_2.png)

![ab_testing_3](images/ab_testing_3.png)

### Logging

![logging](images/logging.png)

### BALANCE LOADING

![cluster](images/cluster.png)

### Cache - USE DJANGO CACHE

### GZIP

![gzip](images/gzip.png)

### NGINX WORKERS

![workers](images/workers.png)

### HTTP1.1 or HTTP2 ( ASGI )

![workers](images/http1_http2.png)

### VARS

* string | int | bool
* set age 7
* $age
* decomposition "include /etc/nginx/mime.types"

### Location ( paths relative to the root )

* uri to path 
* location extends that uri paths
* using with root | alias
* nginx finds server by host or uses default_server
* =, ^=, ~* | ~, /

### PATHS

* /var/log/nginx
* /etc/nginx/nginx.conf
* /srv/

### COMMANDS 

* nginx -t 
* nginx -s reload
* nginx -s reopen