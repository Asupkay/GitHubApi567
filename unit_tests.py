import gitHubAPI

class TestGitHubAPI(object):
    def test_commitCount(self):
        assert len(gitHubAPI.commitCount("ruthylevi")) > 0

    def test_getRepos(self):
        assert len(gitHubAPI.getRepositories("ruthylevi")) > 0

    def test_getCommits(self):
        assert gitHubAPI.getCommits('ruthylevi', 'helloworld') > 0


