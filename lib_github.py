import os, json
from githubutilsapi import GithubUtilsApi

class Utils_Github:
    def __init__(self):
        self.__user = os.environ.get('GITHUB_USER')
        self.__token = os.environ.get('GITHUB_TOKEN')
        self.__url = os.environ.get('GITHUB_URL')
        self.__url_graphql = os.environ.get('GITHUB_URL_GRAPHQL')
        self.github = GithubUtilsApi(self.__user, self.__token, self.__url, self.__url_graphql)
        self.__github_org = os.environ.get('GITHUB_ORG')
        
    def get_list_repos(self):
        repository_list = self.github.list_repositories_all(self.__github_org)
        return_list = [
            {
                'repo_name': item['name'],
            }
            for item in repository_list
        ]
        return return_list


