from lib_github import Utils_Github
from lib_jira import Utils_Jira

jira = Utils_Jira()
github = Utils_Github()

list_repos_jira = jira.get_repository_list()
list_repos_github = github.get_list_repos()

jira_repo_names = {item['repo_name'].lower() for item in list_repos_jira}
github_repo_names = {item['repo_name'].lower() for item in list_repos_github}

pending_create_jira = list(github_repo_names - jira_repo_names)
pending_transition_delete = list(jira_repo_names - github_repo_names)

print("")