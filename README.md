Setup:

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run server:

```shell
pip install -r requirements.txt
uvicorn main:app --reload
```

Run tests:

```shell
python -m unittest tests/api_tests.py
```