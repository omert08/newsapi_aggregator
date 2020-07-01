from functools import lru_cache
import requests
from src import dummyAuthToken


def authControl(headers):
    # split Authorization string into two as 'Basic' and token ,
    # then compare token with dummyAuthToken initialized before.
    if headers['Authorization'].split(' ')[1] == dummyAuthToken:
        return True
    else:
        return False


class NewsApiAggregator():
    _rootEndPoint = "https://newsapi.org/v2/top-headlines"
    _newsapiToken = "5b79a504bb16444996cf59a40804ffc5" # better to keep in os environment.
    _bodyJson = {}

    def __init__(self, query_string=None):
        self.query_string = query_string

    def _linkBuilder(self):
        if self.query_string is None:
            return self._rootEndPoint + "?country=us&apiKey={}".format(self._newsapiToken)
        else:
            return self._rootEndPoint + "?q={}&apiKey={}".format(self.query_string, self._newsapiToken)

    def _bodyParser(self):
        if self._bodyJson['status'] != "ok":
            return False
        result = []
        articles = self._bodyJson['articles']
        for article in articles:
            result.append({'source': 'newsapi', 'link': article['url'], 'headline': article['title']})
        return result

    def fetchNews(self):
        link = self._linkBuilder()
        response = requests.get(link)
        if response.status_code == 200:
            self._bodyJson = response.json()
            result = self._bodyParser()
            if result is not False:
                return result
            else:
                return False
        else:
            return False

