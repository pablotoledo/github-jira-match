import os, json
from atlassian import Jira

class Utils_Jira():
    
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
        
    def __fetch_all_results(self):
            all_issues = []
            start_at = 0
            max_results = 50
            while True:
                response = self.jira.jql(f"project = {self.__jira_project}", start=start_at)
                issues = response.get('issues', [])
                all_issues.extend(issues)
                start_at += max_results
                if len(all_issues) >= response['total']:
                    break
            return all_issues
        
    def get_repository_list(self):
        repository_list = self.__fetch_all_results()
        return_list = [
            {
                'repo_name': item['fields']['summary'],
                'ticket_id': item['key'],
                'ticket_status': item['fields']['status']['name']
            }
            for item in repository_list
        ]
        
        return return_list
    