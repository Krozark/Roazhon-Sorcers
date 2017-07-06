# Roazhon-Sorcers
Roazhon-Sorcers website

# Install

For developers only
--------------

```
gem install sass
```

# For everyone

```
mkvirtualenv raozhon_sorcers --python=python3.6
pip install -r requirements.txt
python manage.py makemigrations
python manage.py makemigrations website
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```


# Deploy on a server using nginx + uWSGI

edit files 
* ```Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_nginx.conf```
* ```Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_uwsgi.conf```

to change :
* ```/home/ubuntu/Documents/Roazhon-Sorcers``` with your project path

```
sudo apt-get install nginx
sudo pip3 install uwsgi
sudo adduser ubuntu www-data
sudo adduser www-data ubuntu
sudo ln -s /home/ubuntu/Documents/Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_nginx.conf  /etc/nginx/sites-enabled/
sudo ln -s /home/ubuntu/Documents/Roazhon-Sorcer/roazhon_sorcers_uwsgi.ini /etc/uwsgi/vassals/
sudo /etc/init.d/nginx restart
```

check url http://localhost:8000/static/website/img/icon.png

add this line to ```/etc/rc.local```

```
sudo /usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
```

## informations

You can find some installation infornation on this page : http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html





