# Coffee

We all love Coffee.

## Run tests

Use the package manager [pip](https://pip.pypa.io/en/stable/) to drink Coffee.

```bash
virtualenv venv --python=python3
source venv/bin/activate
pip install -r requirements
python tests
```

## Building

we use Docker compose, this will install MonogDB and seed it with some data then launch the app

```bash
docker-compose up --build
```

## Usage

Once the app is ready we can use the two endpoints as below

```bash
curl --location --request GET 'http://127.0.0.1:9000/coffee-machines?type=large&water_line=true'
```

this will return something like this
```bash
[
    {
        "_id": {
            "$oid": "5f5bc1300754bcc2f0bb33f1"
        },
        "name": "CM102",
        "type": "LARGE",
        "model": "PREMIUM",
        "water_line": true
    },
    {
        "_id": {
            "$oid": "5f5bc1300754bcc2f0bb33f2"
        },
        "name": "CM103",
        "type": "LARGE",
        "model": "DELUXE",
        "water_line": true
    }
]
```




```bash
curl --location --request GET 'http://127.0.0.1:9000/coffee-pods?flavor=mocha&type=large&size=1'
```

```bash
[
    {
        "_id": {
            "$oid": "5f5bc131deabf55e8b6c56e9"
        },
        "name": "CP131",
        "type": "LARGE",
        "flavor": "MOCHA",
        "size": 1
    }
]
```
 

