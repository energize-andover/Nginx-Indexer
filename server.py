from location import Location

class Server:
    def __init__(self, start_line, end_line, lines):
        self.start_line = start_line
        self.end_line = end_line
        self.lines = lines
        self.server_name = ''
        self.locations = []

        for line_number in range(start_line, end_line + 1):
            line = lines[line_number].rstrip()

            if 'server_name' in line:
                self.server_name = line[line.rfind(' '):line.rfind(';')].replace(' ', '') # Extract the server name from the config file
            elif 'location' in line:
                location_url = line[line.rfind('location') + len('location'):line.rfind('{')].replace(' ', '') # Extract the location from the config file
                self.locations.append(Location(location_url))



    def get_start_line(self):
        return self.start_line

    def get_end_line(self):
        return self.end_line

    def get_link_urls(self):
        links = []
        for location in self.locations:
            links.append('http://' + self.server_name + location.get_url())

        return links
    def get_short_urls(self):
        links = []
        for location in self.locations:
            links.append(location.get_url())

        return links
