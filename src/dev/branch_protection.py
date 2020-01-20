import argparse, json, requests, subprocess
import os

AUTH_TOKEN = os.environ["AUTH_TOKEN"]

def get_auth_token():

    if AUTH_TOKEN is not None:
        return AUTH_TOKEN

    command = ' | '.join(('git credential fill <<< "host=github.com"',
                          'grep -o "password=\w\+"',
                          'cut -d= -f2'
                          ))
    return subprocess.check_output(command, shell=True).strip().decode('utf-8')

def make_api_url(*args):

    return '/'.join(('https://api.github.com', 'repos', *args))

def make_api_headers():

    APPLICATION_HEADER_VALUE='application/vnd.github.loki-preview+json'

    return {
        'Authorization': 'token {:s}'.format(get_auth_token()),
        'Accept': APPLICATION_HEADER_VALUE,
    }

def get_protection(target_repo, branch):

    url = make_api_url(target_repo, 'branches', branch, 'protection')
    return requests.get(url, headers=make_api_headers())

def set_protection(target_repo, branch, data=None):

    url = make_api_url(target_repo, 'branches', branch, 'protection')

    if data is None:
        data = {
            'required_status_checks': None,
            'restrictions': {
                'users': [],
                'teams': [],
            },
            "required_status_checks": None,
            "enforce_admins": None,
            "required_pull_request_reviews": None,
            "allow_force_pushes": True,
            "allow_deletions": False,
        }

    return requests.put(url, headers=make_api_headers(), json=data)


def main():
    parser = argparse.ArgumentParser(description = __doc__)

    parser.add_argument(
        'target_repo',
        help='the target repository (specify as either org/repo or repo)'
    )
    parser.add_argument(
        'target_branch',
        help='the target branch'
    )
    parser.add_argument(
        'action',
        choices=['set', 'get', 'delete'],
        help='action to perform on branch protections'
    )

    def do_and_print_json(fxn, *args):
        print(
            json.dumps(
                fxn(*args).json(),
                sort_keys=True,
                indent=2
            )
        )

    {
        'get':  lambda *args: do_and_print_json(get_protection, *args),
        'set':  lambda *args: do_and_print_json(set_protection, *args),

    }[parser.parse_args().action](
        parser.parse_args().target_repo,
        parser.parse_args().target_branch
    )

if __name__ == "__main__":
    main()
