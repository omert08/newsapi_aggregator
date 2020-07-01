import unittest
from fastapi.testclient import TestClient
from src import app, dummyAuthToken
from src import api

client = TestClient(app)


class TestCases(unittest.TestCase):
    _responseItems = ['headline', 'source', 'link']
    _source = "reddit,newsapi"
    _headers = {"Authorization ": "Basic " + dummyAuthToken}

    def test_listing(self):
        link = '/news?source=' + self._source
        response = client.get(link, headers=self._headers)
        self.assertEqual(response.status_code, 200)
        responseJson = response.json()
        self.assertEqual(len(responseJson['errors']),0) # Check whether there is error messages or not

    def test_search(self):
        searchTerm = "machine"
        link = '/news?source=' + self._source + "&query=" + searchTerm
        response = client.get(link, headers=self._headers)
        self.assertEqual(response.status_code, 200)
        responseJson = response.json()
        self.assertEqual(len(responseJson['errors']),0) # Check whether there is error messages or not


if __name__ == '__main__':
    unittest.main()
