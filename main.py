import os
import shutil

CONFIGURATION_PATHS = [os.path.join(os.sep, 'etc', 'nginx', 'conf.d', 'virtual.conf')]
CONFIG_STORAGE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Nginx-Confs')

def main():
    if(os.path.isdir(CONFIG_STORAGE_PATH)):
        shutil.rmtree(CONFIG_STORAGE_PATH)

    os.makedirs(CONFIG_STORAGE_PATH)

    for path in CONFIGURATION_PATHS:
        path_segments = path.split('/')
        shutil.copyfile(path, os.path.join(CONFIG_STORAGE_PATH, path_segments[len(path_segments) - 1]))

        with open(path, 'r') as config_file:
            for line in config_file:
                global server_name
                line = line.rstrip()

                if 'server_name' in line:
                    server_name = line[line.rfind(' '):line.rfind(';')].replace(' ', '') # Extract the server name from the config file
                    print(server_name)
                elif 'location' in line:
                    location = line[line.rfind('location') + len('location'):line.rfind('{')].replace(' ', '') # Extract the location from the config file
                    print(location)

            print(server_name)
if __name__ == '__main__':
    main()
