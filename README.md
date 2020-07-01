Setup:

```shell
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run server:

```shell
uvicorn main:app --reload
```

Run tests:

```shell
python -m unittest tests/api_tests.py
```



API Features: 

* Source selection (Currently only supports newsapi)
* Query support
* Error Reporting

Examples:

```shell
GET /news?source=reddit,newsapi
```

```shell
GET /news?source=reddit,newsapi&query=trump
```

Response:

```json
{
  "result": [
    {
      "source": "newsapi",
      "link": "http://us.cnn.com/videos/politics/2020/07/01/intelligence-russia-bounty-veteran-rieckhoff-cuomo-cpt-intv-vpx.cnn",
      "headline": "Veteran: Every day Donald Trump is in power, our enemies celebrate - CNN Video"
    }
  ],
  "errors": []
}
```