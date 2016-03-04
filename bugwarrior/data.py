import os
import dbm


DATAFILE = os.path.expanduser(
    os.path.join(os.getenv('TASKDATA', '~/.task'), 'bugwarrior.data'))


def get(key):
    try:
        with dbm.open(DATAFILE) as db:
            return db.get(key)
    except dbm.error:  # File does not exist.
        return None


def set(key, value):
    with dbm.open(DATAFILE, 'c') as db:
        db[key] = value
