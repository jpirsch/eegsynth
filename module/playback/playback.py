import configparser # this is version 3.x specific,on version 2.x it is called "ConfigParser" and has a different API
import sys
import os

#if hasattr(sys, 'frozen'):
#    basis = sys.executable
#else:
basis = sys.argv[0]
installed_folder = os.path.split(basis)[0]

config = configparser.ConfigParser()
config.read(os.path.join(installed_folder, 'playback.ini'))

print(config.get('general', 'name'))
#pattern = r.get(config.get('input','pattern'))

#print(len(sys.argv))
#print(sys.argv[1])
#hotstname=sys.argv[o]


