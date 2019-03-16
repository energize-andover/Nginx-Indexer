import requests
from lxml.html import fromstring
from flask import *
from main import main, configured_servers

main() # initalize configured_servers

app = Flask(__name__)

configured_urls = []
short_urls = []
titles = []

for server in configured_servers:
    configured_urls += server.get_link_urls()
    short_urls += server.get_short_urls()

for url in configured_urls:
    # Pull the title of the webpage from the URL
    r = requests.get(url)
    tree = fromstring(r.content)
    print(tree.findtext('.//title'))

print(configured_urls)

@app.route('/')
def index():
    return render_template("index.html", urls=configured_urls, short_urls=short_urls)

if __name__ == '__main__':
    app.run()
