from config import *
from location import Location


class Server:
    def __init__(self, start_line, end_line, lines):
        self.start_line = start_line
        self.end_line = end_line
        self.lines = lines
        self.server_name = ''
        self.locations = []
        self.is_indexer_host_block = False
        self.short_url_use = []

        for line_number in range(start_line, end_line + 1):
            line = lines[line_number].rstrip()

            if 'server_name' in line:
                # Extract the server name from the config file
                self.server_name = line[line.rfind(' '):line.rfind(';')].replace(' ', '')
            elif 'location' in line:
                # Extract the location from the config file
                location_url = line[line.rfind('location') + len('location'):line.rfind('{')].replace(' ', '')

                if not self.is_indexer_host_block:
                    # Find the proxy pass, if any
                    current_line = line_number + 1
                    while not lines[current_line].rstrip() == '}':
                        line_to_check = lines[current_line].lstrip()

                        if line_to_check.startswith('proxy_pass'):
                            address = line_to_check.rstrip()[10:-1].lstrip()
                            self.is_indexer_host_block = address == ADDRESS_HOSTED
                            break

                        current_line += 1

                self.locations.append(Location(location_url))

    def get_start_line(self):
        return self.start_line

    def get_end_line(self):
        return self.end_line

    def get_link_urls(self):
        links = []
        for location in self.locations:
            self.short_url_use.append(self.is_indexer_host_block)

            links.append('http://' + self.server_name + location.get_url())

        return links

    def get_short_urls(self):
        links = []
        for location in self.locations:
            links.append(location.get_url())

        return links


    def get_short_url_use(self):
        return self.short_url_use