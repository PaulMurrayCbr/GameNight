import os
from migrate.versioning import api

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'gamenight.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  
# Set it to True or False to suppress this warning.
SQLALCHEMY_TRACK_MODIFICATIONS=True

print("Sqlalchemy URI is %s" % SQLALCHEMY_DATABASE_URI)
print("Sqlalchemy migrate repo %s" % SQLALCHEMY_MIGRATE_REPO)

# try :
#     print('Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
# finally:
#     pass

