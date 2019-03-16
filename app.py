import requests
import eventlet
import calendar
from datetime import datetime
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

configured_urls = sorted(configured_urls)
short_urls = sorted(short_urls)

# Pull the title of the webpage from the URL
def get_title(url):
    global title
    try:
        with eventlet.Timeout(2):
            r = requests.get(url) # 2 second ping timeout in case of invalid url
            tree = fromstring(r.content)
            title = tree.findtext('.//title')
            if r.status_code != 200:
                title = ''
    except:
        title = ''

    return title

eventlet.monkey_patch() # Necessary to set timeouts on requests

for index in range(0, len(configured_urls)):
    titles.append(get_title(configured_urls[index]))


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.context_processor
def inject_time_to_all_templates():
    return dict(time=get_time())


@app.route('/')
def index():
    return render_template("index.html", urls=configured_urls, short_urls=short_urls, titles=titles)


def get_time():
    return calendar.timegm(datetime.now().utctimetuple())

if __name__ == '__main__':
    app.run()
