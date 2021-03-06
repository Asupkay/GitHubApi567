import requests
import json

def commitCount(gitHubID):
    repos = getRepositories(gitHubID)
    dict = {};
    for repo in repos:
        repoName = repo["name"]
        dict[repoName] = getCommits(gitHubID, repoName)

    return dict
        

def getRepositories(gitHubID):
    URL = "https://api.github.com/users/" + gitHubID + "/repos"
    r = requests.get(url = URL);
    data = r.json()
    return data

def getCommits(gitHubID, repoName):
    URL = "https://api.github.com/repos/" + gitHubID + "/" + repoName + "/commits"
    r = requests.get(url = URL);
    data = r.json()
    return len(data)

class TestGitHubAPI(object):
    def test_commitCount(self):
        assert len(commitCount("ruthylevi")) > 0

    def test_getRepos(self):
        assert len(getRepositories("ruthylevi")) > 0

    def test_getCommits(self):
        assert getCommits('ruthylevi', 'helloworld') > 0


