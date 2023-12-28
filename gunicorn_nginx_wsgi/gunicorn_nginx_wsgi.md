# Gunicorn, WSGI, and Nginx 

![schema.png](images/schema.png)

### WSGI - Web Server Gateway Interface

* It stays between any server and application

* Specification for prefork server creators

![wsgi_impl.png](images/wsgi_impl.png)

![wsgi_pluses.png](images/wsgi_pluses.png)

### Application Server *preforks python application*

* because of large forking time

* It's Gunicorn or uWSGI

![forking_time.png](images/forking_time.png)

