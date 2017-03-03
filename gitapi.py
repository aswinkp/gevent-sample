import grequests
import requests


class GithubAPI:
    github_root_url = "https://api.github.com"
    def __init__(self, **kwargs):
        self.org = kwargs.get("org")
        self.repos_count = kwargs.get("repos_count")
        self.commitees_count = kwargs.get("commitees_count")

    @classmethod
    def get_org_repos_url(cls,org_name):
        return cls.github_root_url + "/search/repositories?q=user:" + org_name + "&sort=forks&order=desc"

    def get_top_contributors(self):
        r = requests.get(self.get_org_repos_url(org))
        repos_list = r.json()['items'][:self.repos_count]
        # forms grequest object for each of the repos
        rs = (grequests.get(u) for u in [x["contributors_url"] for x in repos_list])
        # fetches the all requests synchronously.
        responses = grequests.map(rs)
        contributors_list = [res.json()[:self.commitees_count] for res in responses]
        for idx, contributors in enumerate(contributors_list):
            repos_list[idx]["contributors_list"] = contributors
        print("Organization Name : {0}".format(org))
        for repo in repos_list:
            print("# Repo: {0} \n  Forks: {2}, URL : {1}".format(repo['name'], repo['url'], repo['forks_count']))
            print("  Top Contributors")
            for contributor in repo['contributors_list']:
                print("  --Contributor: {0}, Contributions: {1}".format(contributor['login'], contributor['contributions']))

if __name__ == "__main__":
    print("Enter org name")
    org = raw_input()
    print("Enter no.of famous repos you need")
    repos_count = int(raw_input())
    print("Enter no of commitees you need for each repo")
    commitees_count = int(raw_input())
    api = GithubAPI(org=org, repos_count=repos_count, commitees_count=commitees_count)
    api.get_top_contributors()




