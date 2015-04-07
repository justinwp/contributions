import requests
import json


PROJECTS_FILE = 'projects.json'
STUDENTS_FILE = 'students.json'
COMMITS_FILE = 'commits.json'

PROJECT_API_URL = 'http://contributions-907.appspot.com/api/project'
STUDENT_API_URL = 'http://contributions-907.appspot.com/api/student'
COMMIT_API_URL = 'http://contributions-907.appspot.com/api/commit'

GITHUB_REPOS = [
    ['justinwp/cs399-band'],
    [],
    [],
    [],
]

DUE_DATE_MAPPING = ["2015-01-23", "2015-02-06", "2015-02-20", "2015-04-03"]


def get_repo(repo_name, project_number):
    print "Getting Repo: %s" % repo_name

    # Create project in database
    data = {
        "project_number": project_number,
        "repo_name": repo_name
    }
    response = requests.post(PROJECT_API_URL, data=json.dumps(data))

    # error handling for posting project

    if response.status_code == 200:
        pass
    elif response.status_code == 409:
        # already exists
        response = requests.get(PROJECT_API_URL + "/%s" % repo_name)
    else:
        raise Exception()

    project = response.json

    # get all of the commits and contributors from the commits
    parse_commits(project)

    print "Found %d Commits" % project['commit_count']

    print "Saving Number of Commits to Project"
    update = {
        "project_number": project_number,
        "repo_name": repo_name
    }

    # response = requests.put(PROJECT_API_URL + "/%s" % repo_name, data=json.dumps(update))


def save_repo(data):
    pass


def parse_commits(project):
    """
    Gets all commits for the repo
    :param project:
    :return: None
    """
    project['commit_count'] = 0
    print "Getting Commits for: %s" % project['repo_name']
    # TODO get list of all commits from all pages

    # TODO Parse commit
    # Add students found

    # Increment commit counter
    project['commit_count'] += 1


def save_commit(data):
    pass


if __name__ == "__main__":
    for i, project_list in enumerate(GITHUB_REPOS):
        # projects are not zero based
        project_number = i + 1

        print "*** Getting Repos for Project #%d ***" % project_number

        for project in project_list:
            get_repo(project, project_number)