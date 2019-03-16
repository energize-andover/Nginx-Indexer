import os
import shutil
import inspect
from server import Server

debug_mode = True
CONFIGURATION_PATHS = [os.path.join(os.sep, 'etc', 'nginx', 'conf.d', 'virtual.conf')]
CONFIG_STORAGE_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Nginx-Confs')

global configured_servers
configured_servers = []

def main():
    if os.path.isdir(CONFIG_STORAGE_PATH) and not debug_mode:
        shutil.rmtree(CONFIG_STORAGE_PATH)

    if not debug_mode:
        os.makedirs(CONFIG_STORAGE_PATH)

    for path in CONFIGURATION_PATHS:
        path_segments = path.split('/')
        output_path = os.path.join(CONFIG_STORAGE_PATH, path_segments[len(path_segments) - 1])
        if not debug_mode:
            shutil.copyfile(path, output_path)

        with open(output_path, 'r') as config_file:
            global server_name
            lines = config_file.readlines()
            for line_number in range(0, len(lines)):
                line = lines[line_number].rstrip()

                if 'server' in line and '{' in line:
                    # The begining of the definition of a server
                    start_line = line_number

                    while not line.startswith('}'):
                        line_number += 1
                        line = lines[line_number].rstrip()

                    end_line = line_number
                    configured_servers.append(Server(start_line, end_line, lines))


if __name__ == '__main__':
    main()
