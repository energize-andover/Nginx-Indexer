# Nginx-Indexer
Indexes our Nginx server and creates a homepage for its locations.

## Screenshots
<p align="center">
<img src="https://i.imgur.com/XWZ5mDc.png?1" alt="A screenshot of Nginx-Indexer running on our server">
  <em>A screenshot of Nginx-Indexer running on our server</em>
</p>

## Installation
1) Clone this repository
2) Install the requirements (you can use `pip install -r requirements.txt` to automatically install all of them)
3) Edit `CONFIGURATION_PATHS` in `main.py` like so: Add the paths to every Nginx configuration file that initializes a location you would like indexed (using `os.path.join()` is recommended to guarantee the paths are correct)
4) Run `app.py` and visit `localhost:5000`. The site should be live.
5) If you would like to host this page on your own Nginx server's root, we reccomend using `gunicorn` (should automatically be installed from `requirements.txt`).

## Credits
This project was created and installed onto the server by [Daniel Ivanovich](https://ivanovich.us) in March of 2019. 
