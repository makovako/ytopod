# UWSGI

- application server
- socket - for some esternal web server
- http - for localhost deploy

# Flask

- `export FLASK_APP=run.py`
- `export FLASK_ENV=development`
- `flask run`

# Flask async

- by default flask is blocking(synchronous) and there is no easy way to change it
- some solutions
  - quart - flask with async
  - celery - task queue, separate service
- used solution - threading
  - start new thread for new task
  - pass app context to it, so you can access app, db, request and other stuff

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