from typing import Optional
from functools import lru_cache
from src import app
from src.controllers import authControl, NewsApiAggregator
from fastapi import Header


@app.get("/news")
@lru_cache()
def readNews(source:str="reddit,newsapi",query:str = None):
    result = []
    errors = []

    # Auth Control
    # status = authControl(headers)
    # if status is False:
    #     errors.append('Authentication is failed')
    #     return {"result": result, "errors": errors},401

    source_list = source.split(',')

    for item in source_list:
        if item == 'newsapi':
            aggrInstance = NewsApiAggregator(query_string=query)
            response = aggrInstance.fetchNews()
            if response is not False:
                result.extend(response)
            else:
                errors.append('Something went wrong in newsapi aggregator')

        # Another api can be added here with another if clause

    return {"result": result, "errors": errors}
