# mediascribe
Web application for automatic speech recognition of web-based AV content


## Development

either:

 - DIY in a virtualenv, or
 - docker-compose


### In a virtualenv

#### Install requirements

```
pip install -r requirements.txt
```

#### Configure the path

```
export PYTHONPATH = src:$PYTHONPATH
```

#### Run the application

```
uvicorn mediascribe.main:app --reload
```


### Using docker-compose

TODO


## API documentation

Endpoints:

 - `/schema` (default. Alias to redoc)
 - `/schema/openapi.yml`
 - `/schema/openapi.json`
 - `/schema/redoc`
 - `/schema/swagger`
 - `/schema/elements`
