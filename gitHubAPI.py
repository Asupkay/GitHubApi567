import requests
import json

def commitCount(gitHubID):
    repos = getRepositories(gitHubID)
    print(repos)
    dict = {};
    for repo in repos:
        repoName = repo["name"]
        dict[repoName] = getCommits(gitHubID, repoName)

    print(dict)
        

def getRepositories(gitHubID):
    URL = "https://api.github.com/users/" + gitHubID + "/repos"
    r = requests.get(url = URL);
    data = r.json()
    return data

def getCommits(gitHubID, repoName):
    URL = "https://api.github.com/repos/" + gitHubID + "/" + repoName + "/commits"
    r = requests.get(url = URL);
    data = r.json()
    print(data)
    return len(data)

commitCount("Bsoong");
