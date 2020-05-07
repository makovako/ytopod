# UWSGI

- application server
- socket - for some esternal web server
- http - for localhost deploy

# Flask

- `export FLASK_APP=run.py`
- `export FLASK_ENV=development`
- `flask run`

## Some variables

-`request.url`- http://domain:port/path
-`request.base_url`- http://domain:port/path
-`request.url_root`- http://domain:port/
-`request.host`- domain:port
-`request.host_url`- http://domain:port/
-`request.trusted_hosts`- None

# NGINX

- web server
- uwsgi pass  either network or socket file