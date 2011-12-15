from bugwarrior.config import load_config
from bugwarrior.services import aggregate_issues
from bugwarrior.db import synchronize


def pull():
    # Load our config file
    config = load_config()

    # Get all the issues.  This can take a while.
    issues = aggregate_issues(config)

    # Stuff them in the taskwarrior db as necessary
    synchronize(issues)
