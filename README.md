# mediascribe
Web application for automatic speech recognition of web-based AV content


## Development

either:

 - docker-compose, or
 - DIY in a virtualenv

### Using docker-compose

```
docker compose up
```

### In a virtualenv

#### Install requirements

```
pip install -r requirements-dev.txt
```

#### Configure the path

```
export PYTHONPATH = src:$PYTHONPATH
```

#### Run the application

```
uvicorn mediascribe.main:app --reload
```


### Code style

```
black src
```


## API documentation

Endpoints:

 - `/schema` (default. Alias to redoc)
 - `/schema/openapi.yml`
 - `/schema/openapi.json`
 - `/schema/redoc`
 - `/schema/swagger`
 - `/schema/elements`
