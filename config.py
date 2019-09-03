# NGINX-INDEXER CONFIGURATION FILE: USE DEFAULT AS A SAMPLE #
import os

'''
    # Utilize the os package to form your paths:
    # The method os.path.join(part1, part2, ... lastPart) forms a properly-formatted path for your OS. 
    # The variable os.sep represents the proper path separator for your os (i.e. '/')
    # The method os.path.dirname(os.path.realpath(__file__) returns the path to the directory in which this file is 
      stored, named Nginx-Indexer by default. It may be useful os.path.join() it in your CONFIG_STORAGE_PATH to store
      the copied configuration files in the same directory as the rest of the files needed by the indexer
'''

# A list ([item1, item2, ... lastItem]) of paths to the nginx configuration files that will be indexed
CONFIGURATION_PATHS = [os.path.join(os.sep, 'etc', 'nginx', 'conf.d', 'virtual.conf')]

# The path to the folder in which the configuration files will be copied to and temporarily stored for indexing
CONFIG_STORAGE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Nginx-Confs')

STARTUP_DELAY = 30  # How many seconds to wait to start indexing after app.py is run, in seconds. Allows apps to boot up

'''
    # BE SURE TO RUN git update-index --skip-worktree config.py AFTER MAKING CHANGES TO THIS FILE FOR THE FIRST TIME!
      Doing so will keep your machine-specific configurations out of the repository, allowing the defaults to remain 
      untouched. 
'''