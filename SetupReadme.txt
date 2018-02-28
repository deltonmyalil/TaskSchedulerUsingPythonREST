oot@kali:~# cd Desktop
root@kali:~/Desktop# virtualenv renv
Using base prefix '/usr'
New python executable in /root/Desktop/renv/bin/python3
Also creating executable in /root/Desktop/renv/bin/python
Installing setuptools, pip, wheel...done.
root@kali:~/Desktop# cd renv
root@kali:~/Desktop/renv# dir
bin  include  lib  pip-selfcheck.json
root@kali:~/Desktop/renv# cd bin
root@kali:~/Desktop/renv/bin# dir
activate       activate_this.py  pip	 python     python-config
activate.csh   easy_install	 pip3	 python3    wheel
activate.fish  easy_install-3.6  pip3.6  python3.6
root@kali:~/Desktop/renv/bin# source ./activate
(renv) root@kali:~/Desktop/renv/bin# pip3 install django
Collecting django
  Using cached Django-2.0.2-py3-none-any.whl
Collecting pytz (from django)
  Using cached pytz-2018.3-py2.py3-none-any.whl
Installing collected packages: pytz, django
Successfully installed django-2.0.2 pytz-2018.3
(renv) root@kali:~/Desktop/renv/bin# pip install djangorestframework
Collecting djangorestframework
  Downloading djangorestframework-3.7.7-py2.py3-none-any.whl (1.1MB)
    100% |████████████████████████████████| 1.1MB 322kB/s 
Installing collected packages: djangorestframework
Successfully installed djangorestframework-3.7.7
(renv) root@kali:~/Desktop/renv/bin# cd ..
(renv) root@kali:~/Desktop/renv# dir
bin  include  lib  pip-selfcheck.json
(renv) root@kali:~/Desktop/renv# django-admin startproject rest
(renv) root@kali:~/Desktop/renv# dir
bin  include  lib  pip-selfcheck.json  rest
(renv) root@kali:~/Desktop/renv# cd rest
(renv) root@kali:~/Desktop/renv/rest# django admin startapp restapp
bash: django: command not found
(renv) root@kali:~/Desktop/renv/rest# django-admin startapp restapp
(renv) root@kali:~/Desktop/renv/rest# cd restapp
(renv) root@kali:~/Desktop/renv/rest/restapp# dir
admin.py  apps.py  __init__.py	migrations  models.py  tests.py  views.py
(renv) root@kali:~/Desktop/renv/rest/restapp# cd ..
(renv) root@kali:~/Desktop/renv/rest# python3 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 14 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

February 27, 2018 - 10:33:37
Django version 2.0.2, using settings 'rest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
[27/Feb/2018 10:33:54] "GET / HTTP/1.1" 200 16348
[27/Feb/2018 10:33:57] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[27/Feb/2018 10:33:57] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 80304
[27/Feb/2018 10:33:57] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 82564
[27/Feb/2018 10:33:57] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 81348
Not Found: /favicon.ico
[27/Feb/2018 10:33:57] "GET /favicon.ico HTTP/1.1" 404 1970
^C(renv) root@kali:~/Desktop/renv/rest# 

