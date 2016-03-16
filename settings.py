import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {}

config['repo'] = os.environ.get("REPO")
config['owner'] = os.environ.get("OWNER")

config['user'] = os.environ.get("USER")
config['auth_token'] = os.environ.get("AUTH_TOKEN")
config['post_secret'] = os.environ.get("HOOK_SECRET")
config['merge_re'] = os.environ.get("MERGE_REGEX")
config['path_to_repo'] = os.environ.get("REPO_PATH")
config['repo_branch'] = os.environ.get("REPO_BRANCH")
config['repo_remote'] = os.environ.get("REPO_REMOTE")
config['trusted_users'] = map(str.strip, os.environ.get("TRUSTED_USERS").split(","))
