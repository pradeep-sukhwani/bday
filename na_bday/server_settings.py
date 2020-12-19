import os

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g2=6%+mh16l1!udp*ykcrjm4c5#z2@#+pnu&x!12b4u1w#9y22'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'database': 'na_bday',
            'user': 'root',
            'password': 'root'
        },
    }
}
