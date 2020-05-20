"""Create an issue on github.com using the given parameters."""

import os
import sys
import requests
import json

from datetime import datetime
from argparse import ArgumentParser


def current_time_formatted():
    """GitHub API accepts timestamp in following format: '2020-03-10T16:00:00Z'."""
    return datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')


def make_github_issue(title, body=None, created_at=None, closed_at=None, updated_at=None,
                      assignee=None, milestone=None, closed=None, labels=None, token=None,
                      organization=None, repository=None):
    """Create an issue on github.com using the given parameters."""
    # Url to create issues via POST
    url = 'https://api.github.com/repos/%s/%s/import/issues' % (organization, repository)

    # Headers
    headers = {
        "Authorization": "token %s" % token,
        "Accept": "application/vnd.github.golden-comet-preview+json"
    }

    # Create our issue
    data = {'issue': {'title': title,
                      'body': body,
                      'created_at': created_at,
                      'assignee': assignee}}

    payload = json.dumps(data)

    # Add the issue to our repository
    response = requests.request("POST", url, data=payload, headers=headers)
    if response.status_code == 202:
        print('Successfully created Issue "%s"' % title)
    else:
        print('Could not create Issue "%s"' % title)
        print('Response:', response.content)


def cli_arguments():
    """Retrieve all CLI arguments."""
    parser = ArgumentParser()

    # Authentication for user filing issue (must have read/write access to
    # repository to add issue to)
    parser.add_argument("-t", "--token", dest="token", help="authentication token",
                        action="store", default=None, type=str, required=True)

    # The repository to add this issue to
    parser.add_argument("-o", "--organization", dest="organization",
                        help="organization or repository owner",
                        action="store", default=None, type=str, required=True)
    parser.add_argument("-r", "--repository", dest="repository", help="repository name",
                        action="store", default=None, type=str, required=True)

    # Issue-related options
    parser.add_argument("-i", "--title", dest="title", help="issue title",
                        action="store", default=None, type=str, required=True)

    parser.add_argument("-b", "--body", dest="body", help="body (text) of an issue",
                        action="store", default=None, type=str, required=True)

    parser.add_argument("-a", "--assignee", dest="assignee", help="default assignee",
                        action="store", default=None, type=str, required=True)

    # Other options
    parser.add_argument("-v", "--verbose", dest="verbose", help="make operations verbose",
                        action="store_true", default=None)

    return parser.parse_args()


def main():
    """Entry point to this script."""
    timestamp = current_time_formatted()
    args = cli_arguments()
    make_github_issue(args.title, body=args.body, created_at=timestamp, assignee=args.assignee,
                      organization=args.organization, repository=args.repository, token=args.token)


if __name__ == "__main__":
    main()
