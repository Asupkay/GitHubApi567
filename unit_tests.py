from unittest import mock
from requests.models import Response
import gitHubAPI

commitReturn = [
    {
        "sha": "691c42bbb77a49293f69eacddd803bdc0cfd91e2",
        "node_id": "MDY6Q29tbWl0NTExNjYyODA6NjkxYzQyYmJiNzdhNDkyOTNmNjllYWNkZGQ4MDNiZGMwY2ZkOTFlMg==",
        "commit": {
            "author": {
                "name": "asupkay",
                "email": "asupkay1124@gmail.com",
                "date": "2016-02-05T18:55:02Z"
            },
            "committer": {
                "name": "asupkay",
                "email": "asupkay1124@gmail.com",
                "date": "2016-02-05T18:55:02Z"
            },
            "message": "Added description to README.md file explaining project",
            "tree": {
                "sha": "7ac126874d471fedb6764f44c69b9099f7fc73c9",
                "url": "https://api.github.com/repos/Asupkay/GameJam7/git/trees/7ac126874d471fedb6764f44c69b9099f7fc73c9"
            },
            "url": "https://api.github.com/repos/Asupkay/GameJam7/git/commits/691c42bbb77a49293f69eacddd803bdc0cfd91e2",
            "comment_count": 0,
            "verification": {
                "verified": False,
                "reason": "unsigned",
                "signature": None,
                "payload": None
            }
        },
        "url": "https://api.github.com/repos/Asupkay/GameJam7/commits/691c42bbb77a49293f69eacddd803bdc0cfd91e2",
        "html_url": "https://github.com/Asupkay/GameJam7/commit/691c42bbb77a49293f69eacddd803bdc0cfd91e2",
        "comments_url": "https://api.github.com/repos/Asupkay/GameJam7/commits/691c42bbb77a49293f69eacddd803bdc0cfd91e2/comments",
        "author": {
            "login": "Asupkay",
            "id": 17088356,
            "node_id": "MDQ6VXNlcjE3MDg4MzU2",
            "avatar_url": "https://avatars3.githubusercontent.com/u/17088356?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Asupkay",
            "html_url": "https://github.com/Asupkay",
            "followers_url": "https://api.github.com/users/Asupkay/followers",
            "following_url": "https://api.github.com/users/Asupkay/following{/other_user}",
            "gists_url": "https://api.github.com/users/Asupkay/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Asupkay/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Asupkay/subscriptions",
            "organizations_url": "https://api.github.com/users/Asupkay/orgs",
            "repos_url": "https://api.github.com/users/Asupkay/repos",
            "events_url": "https://api.github.com/users/Asupkay/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Asupkay/received_events",
            "type": "User",
            "site_admin": False
        },
        "committer": {
            "login": "Asupkay",
            "id": 17088356,
            "node_id": "MDQ6VXNlcjE3MDg4MzU2",
            "avatar_url": "https://avatars3.githubusercontent.com/u/17088356?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Asupkay",
            "html_url": "https://github.com/Asupkay",
            "followers_url": "https://api.github.com/users/Asupkay/followers",
            "following_url": "https://api.github.com/users/Asupkay/following{/other_user}",
            "gists_url": "https://api.github.com/users/Asupkay/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Asupkay/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Asupkay/subscriptions",
            "organizations_url": "https://api.github.com/users/Asupkay/orgs",
            "repos_url": "https://api.github.com/users/Asupkay/repos",
            "events_url": "https://api.github.com/users/Asupkay/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Asupkay/received_events",
            "type": "User",
            "site_admin": False
        },
        "parents": [
            {
            "sha": "5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
            "url": "https://api.github.com/repos/Asupkay/GameJam7/commits/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
            "html_url": "https://github.com/Asupkay/GameJam7/commit/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a"
            }
        ]
    },
    {
        "sha": "5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
        "node_id": "MDY6Q29tbWl0NTExNjYyODA6NWIxNmZkZDk2ZmNkMmY1ZGQwZWQ2YmY0NDMwNDdhOWRmN2EyZjg2YQ==",
        "commit": {
            "author": {
                "name": "asupkay",
                "email": "asupkay1124@gmail.com",
                "date": "2016-02-05T18:44:07Z"
            },
            "committer": {
                "name": "asupkay",
                "email": "asupkay1124@gmail.com",
                "date": "2016-02-05T18:44:07Z"
            },
            "message": "first commit",
            "tree": {
                "sha": "8e2c90aebc2d13769699d1813375d7bfd753be77",
                "url": "https://api.github.com/repos/Asupkay/GameJam7/git/trees/8e2c90aebc2d13769699d1813375d7bfd753be77"
            },
            "url": "https://api.github.com/repos/Asupkay/GameJam7/git/commits/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
            "comment_count": 0,
            "verification": {
                "verified": False,
                "reason": "unsigned",
                "signature": None,
                "payload": None
            }
        },
        "url": "https://api.github.com/repos/Asupkay/GameJam7/commits/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
        "html_url": "https://github.com/Asupkay/GameJam7/commit/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a",
        "comments_url": "https://api.github.com/repos/Asupkay/GameJam7/commits/5b16fdd96fcd2f5dd0ed6bf443047a9df7a2f86a/comments",
        "author": {
            "login": "Asupkay",
            "id": 17088356,
            "node_id": "MDQ6VXNlcjE3MDg4MzU2",
            "avatar_url": "https://avatars3.githubusercontent.com/u/17088356?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Asupkay",
            "html_url": "https://github.com/Asupkay",
            "followers_url": "https://api.github.com/users/Asupkay/followers",
            "following_url": "https://api.github.com/users/Asupkay/following{/other_user}",
            "gists_url": "https://api.github.com/users/Asupkay/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Asupkay/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Asupkay/subscriptions",
            "organizations_url": "https://api.github.com/users/Asupkay/orgs",
            "repos_url": "https://api.github.com/users/Asupkay/repos",
            "events_url": "https://api.github.com/users/Asupkay/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Asupkay/received_events",
            "type": "User",
            "site_admin": False
        },
        "committer": {
            "login": "Asupkay",
            "id": 17088356,
            "node_id": "MDQ6VXNlcjE3MDg4MzU2",
            "avatar_url": "https://avatars3.githubusercontent.com/u/17088356?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Asupkay",
            "html_url": "https://github.com/Asupkay",
            "followers_url": "https://api.github.com/users/Asupkay/followers",
            "following_url": "https://api.github.com/users/Asupkay/following{/other_user}",
            "gists_url": "https://api.github.com/users/Asupkay/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Asupkay/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Asupkay/subscriptions",
            "organizations_url": "https://api.github.com/users/Asupkay/orgs",
            "repos_url": "https://api.github.com/users/Asupkay/repos",
            "events_url": "https://api.github.com/users/Asupkay/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Asupkay/received_events",
            "type": "User",
            "site_admin": False
        },
        "parents": []
    }
]

reposReturn = [
    {
        "id": 156753014,
        "node_id": "MDEwOlJlcG9zaXRvcnkxNTY3NTMwMTQ=",
        "name": "Algorithms",
        "full_name": "Bsoong/Algorithms",
        "private": False,
        "owner": {
            "login": "Bsoong",
            "id": 25209141,
            "node_id": "MDQ6VXNlcjI1MjA5MTQx",
            "avatar_url": "https://avatars1.githubusercontent.com/u/25209141?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Bsoong",
            "html_url": "https://github.com/Bsoong",
            "followers_url": "https://api.github.com/users/Bsoong/followers",
            "following_url": "https://api.github.com/users/Bsoong/following{/other_user}",
            "gists_url": "https://api.github.com/users/Bsoong/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Bsoong/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Bsoong/subscriptions",
            "organizations_url": "https://api.github.com/users/Bsoong/orgs",
            "repos_url": "https://api.github.com/users/Bsoong/repos",
            "events_url": "https://api.github.com/users/Bsoong/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Bsoong/received_events",
            "type": "User",
            "site_admin": False
        },
        "html_url": "https://github.com/Bsoong/Algorithms",
        "description": "Stevens course CS - 385.",
        "fork": False,
        "url": "https://api.github.com/repos/Bsoong/Algorithms",
        "forks_url": "https://api.github.com/repos/Bsoong/Algorithms/forks",
        "keys_url": "https://api.github.com/repos/Bsoong/Algorithms/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/Bsoong/Algorithms/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/Bsoong/Algorithms/teams",
        "hooks_url": "https://api.github.com/repos/Bsoong/Algorithms/hooks",
        "issue_events_url": "https://api.github.com/repos/Bsoong/Algorithms/issues/events{/number}",
        "events_url": "https://api.github.com/repos/Bsoong/Algorithms/events",
        "assignees_url": "https://api.github.com/repos/Bsoong/Algorithms/assignees{/user}",
        "branches_url": "https://api.github.com/repos/Bsoong/Algorithms/branches{/branch}",
        "tags_url": "https://api.github.com/repos/Bsoong/Algorithms/tags",
        "blobs_url": "https://api.github.com/repos/Bsoong/Algorithms/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/Bsoong/Algorithms/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/Bsoong/Algorithms/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/Bsoong/Algorithms/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/Bsoong/Algorithms/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/Bsoong/Algorithms/languages",
        "stargazers_url": "https://api.github.com/repos/Bsoong/Algorithms/stargazers",
        "contributors_url": "https://api.github.com/repos/Bsoong/Algorithms/contributors",
        "subscribers_url": "https://api.github.com/repos/Bsoong/Algorithms/subscribers",
        "subscription_url": "https://api.github.com/repos/Bsoong/Algorithms/subscription",
        "commits_url": "https://api.github.com/repos/Bsoong/Algorithms/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/Bsoong/Algorithms/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/Bsoong/Algorithms/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/Bsoong/Algorithms/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/Bsoong/Algorithms/contents/{+path}",
        "compare_url": "https://api.github.com/repos/Bsoong/Algorithms/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/Bsoong/Algorithms/merges",
        "archive_url": "https://api.github.com/repos/Bsoong/Algorithms/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/Bsoong/Algorithms/downloads",
        "issues_url": "https://api.github.com/repos/Bsoong/Algorithms/issues{/number}",
        "pulls_url": "https://api.github.com/repos/Bsoong/Algorithms/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/Bsoong/Algorithms/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/Bsoong/Algorithms/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/Bsoong/Algorithms/labels{/name}",
        "releases_url": "https://api.github.com/repos/Bsoong/Algorithms/releases{/id}",
        "deployments_url": "https://api.github.com/repos/Bsoong/Algorithms/deployments",
        "created_at": "2018-11-08T18:44:07Z",
        "updated_at": "2018-12-19T05:32:29Z",
        "pushed_at": "2018-12-19T05:32:28Z",
        "git_url": "git://github.com/Bsoong/Algorithms.git",
        "ssh_url": "git@github.com:Bsoong/Algorithms.git",
        "clone_url": "https://github.com/Bsoong/Algorithms.git",
        "svn_url": "https://github.com/Bsoong/Algorithms",
        "homepage": None,
        "size": 3666,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "Shell",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 0,
        "mirror_url": None,
        "archived": False,
        "open_issues_count": 0,
        "license": None,
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "master"
    },
    {
        "id": 162481048,
        "node_id": "MDEwOlJlcG9zaXRvcnkxNjI0ODEwNDg=",
        "name": "bsoong.github.io",
        "full_name": "Bsoong/bsoong.github.io",
        "private": False,
        "owner": {
            "login": "Bsoong",
            "id": 25209141,
            "node_id": "MDQ6VXNlcjI1MjA5MTQx",
            "avatar_url": "https://avatars1.githubusercontent.com/u/25209141?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/Bsoong",
            "html_url": "https://github.com/Bsoong",
            "followers_url": "https://api.github.com/users/Bsoong/followers",
            "following_url": "https://api.github.com/users/Bsoong/following{/other_user}",
            "gists_url": "https://api.github.com/users/Bsoong/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/Bsoong/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/Bsoong/subscriptions",
            "organizations_url": "https://api.github.com/users/Bsoong/orgs",
            "repos_url": "https://api.github.com/users/Bsoong/repos",
            "events_url": "https://api.github.com/users/Bsoong/events{/privacy}",
            "received_events_url": "https://api.github.com/users/Bsoong/received_events",
            "type": "User",
            "site_admin": False
        },
        "html_url": "https://github.com/Bsoong/bsoong.github.io",
        "description": "The files for the Website I created which is featured at www.Bsoong.com,",
        "fork": False,
        "url": "https://api.github.com/repos/Bsoong/bsoong.github.io",
        "forks_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/forks",
        "keys_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/teams",
        "hooks_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/hooks",
        "issue_events_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/issues/events{/number}",
        "events_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/events",
        "assignees_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/assignees{/user}",
        "branches_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/branches{/branch}",
        "tags_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/tags",
        "blobs_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/languages",
        "stargazers_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/stargazers",
        "contributors_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/contributors",
        "subscribers_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/subscribers",
        "subscription_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/subscription",
        "commits_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/contents/{+path}",
        "compare_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/merges",
        "archive_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/downloads",
        "issues_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/issues{/number}",
        "pulls_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/labels{/name}",
        "releases_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/releases{/id}",
        "deployments_url": "https://api.github.com/repos/Bsoong/bsoong.github.io/deployments",
        "created_at": "2018-12-19T19:21:32Z",
        "updated_at": "2019-02-26T20:57:31Z",
        "pushed_at": "2019-02-26T20:57:30Z",
        "git_url": "git://github.com/Bsoong/bsoong.github.io.git",
        "ssh_url": "git@github.com:Bsoong/bsoong.github.io.git",
        "clone_url": "https://github.com/Bsoong/bsoong.github.io.git",
        "svn_url": "https://github.com/Bsoong/bsoong.github.io",
        "homepage": "https://www.bsoong.com",
        "size": 6333,
        "stargazers_count": 1,
        "watchers_count": 1,
        "language": "CSS",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 0,
        "mirror_url": None,
        "archived": False,
        "open_issues_count": 1,
        "license": None,
        "forks": 0,
        "open_issues": 1,
        "watchers": 1,
        "default_branch": "master"
    },
]



class TestGitHubAPI(object):
    def test_commitCount(self):
        mock_getCommits_patcher = mock.patch('gitHubAPI.getCommits')
        mock_getCommits = mock_getCommits_patcher.start()
        mock_getCommits.return_value = 20

        mock_getRepos_patcher = mock.patch('gitHubAPI.getRepositories')
        mock_getRepos = mock_getRepos_patcher.start()
        mock_getRepos.return_value = reposReturn 

        commitCount = gitHubAPI.commitCount("bSoong")

        mock_getCommits_patcher.stop()
        mock_getRepos_patcher.stop()


        matchedCount = {'Algorithms': 20, 'bsoong.github.io': 20}
        shared_items = {k: commitCount[k] for k in commitCount if k in matchedCount and commitCount[k] == matchedCount[k]}
        assert len(shared_items) == 2

    def test_getRepos(self):
        mock_get_patcher = mock.patch('gitHubAPI.requests.get')
        mock_get = mock_get_patcher.start()
        the_response = mock.Mock(spec=Response)
        the_response.json.return_value = reposReturn
        mock_get.return_value = the_response
        commits = gitHubAPI.getRepositories('Bsoong')

        mock_get_patcher.stop()
        assert len(commits) == 2

    def test_getCommits(self):
        mock_get_patcher = mock.patch('gitHubAPI.requests.get')
        mock_get = mock_get_patcher.start()
        the_response = mock.Mock(spec=Response)
        the_response.json.return_value = commitReturn
        mock_get.return_value = the_response
        commits = gitHubAPI.getCommits('asupkay', 'GameJam7')
        mock_get_patcher.stop()

        assert commits == 2

