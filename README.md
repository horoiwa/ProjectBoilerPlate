# Getting started

## Local env

`cd project && poetry run --no-root`

`poetry run python -V`

`poetry run pytest`

## Container env

`sudo ./cmd.sh up`

`sudo ./cmd.sh login`

`cd project && python -V && pytest`


## Product env

`sudo ./cmd.sh product`



Update document

```
cd project
poetry run sphinx-apidoc -e -f -o ./docs .
cd docs && make html
```
