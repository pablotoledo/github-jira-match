import os
from githubutilsapi import GithubUtilsApi

class Utils_Github:
    def __init__(self):
        self.__user = os.environ.get('GITHUB_USER')
        self.__token = os.environ.get('GITHUB_TOKEN')
        self.__url = os.environ.get('GITHUB_URL')
        self.__url_graphql = os.environ.get('GITHUB_URL_GRAPHQL')
        self.github = GithubUtilsApi(self.__token, self.__url)
        
    


