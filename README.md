# Roazhon-Sorcers
Roazhon-Sorcers website

# Install

For developers only
--------------

```
gem install sass
python manage.py runserver --settings=roazhon_rcers.settings.dev
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
* ```/home/user/Roazhon-Sorcers``` with your project path


## Prepare the server

```
sudo apt-get install nginx
sudo pip3 install uwsgi
sudo adduser ubuntu www-data
sudo adduser www-data ubuntu
sudo mkdir -p /etc/uwsgi/vassals
```

## Add new site + configuration
```
sudo ln -s /home/user/Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_nginx.conf  /etc/nginx/sites-enabled/
sudo ln -s /home/user/Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_uwsgi.ini /etc/uwsgi/vassals/
```

copy file ```roazhon_sorcers/settings/dev.py``` into ```roazhon_sorcers/settings/prod.py``` and change value of
* DEV to False
* SECRET_KEY to a new one
* fill ALLOWED_HOSTS
* fill DATABASES dict


## Start uwsgi

 use ONE of those commande to start uwsgi
```
uwsgi --ini /home/user/Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_uwsgi.ini
# OR
sudo /usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
```

## Restart ngnix

```
sudo /etc/init.d/nginx restart
```
## Make some checks

* check url http://localhost:80
* check url http://localhost:80/static/website/img/icon.png
* check url http://localhost:80/admin

## Update rc.local

Add the line use in section _Start uwsgi_ to ```/etc/rc.local```

```
uwsgi --ini /home/user/Roazhon-Sorcers/roazhon_sorcers/roazhon_sorcers_uwsgi.ini
# OR
sudo /usr/local/bin/uwsgi --emperor /etc/uwsgi/vassals --uid www-data --gid www-data --daemonize /var/log/uwsgi-emperor.log
```

## More installation informations

You can find some installation infornation on this page : http://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html
