
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn_hello.conf.py   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/gunicorn_ask.conf.py   /etc/gunicorn.d/ask.py
sudo killall -9 gunicorn
sudo gunicorn -c /etc/gunicorn.d/hello.py hello:app &
sudo gunicorn -c /etc/gunicorn.d/ask.py ask:wsgi &
#﻿sudo /etc/init.d/mysql start﻿



