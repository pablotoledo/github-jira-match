from lib_github import Utils_Github
from lib_jira import Utils_Jira

jira = Utils_Jira()
github = Utils_Github()

list_repos_jira = jira.get_repository_list()
list_repos_github = github.get_list_repos()

print("")