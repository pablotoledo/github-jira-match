import os, json
from atlassian import Jira

class JiraLib(Jira):
    
    def __init__(self):
        self.__url = os.environ.get("JIRA_URL")
        self.__user = os.environ.get("JIRA_USER")
        self.__password = os.environ.get("JIRA_TOKEN")
        self.jira = Jira(
            url=self.__url,
            username=self.__user,
            password=self.__password
        )
        self.__jira_project = os.environ.get("JIRA_PROJECT")
        
    def get_repository_list(self):
        # TODO
        # Only needed a list of repos, name, ticket id, ticket status
        repository_list = self.jira.jql("project = " + self.__jira_project)
    
    