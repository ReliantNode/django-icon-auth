# django-icon-auth

![django-icon-auth](https://dl.dropboxusercontent.com/s/5708iw4r6b9f2x7/2020-02-17%2017.40.57.gif)

## Installation

1. `pip install https://github.com/ReliantNode/django-icon-auth/archive/master.zip`

## Usage
1. Add `'iconauth'` to the `INSTALLED_APPS` setting
2. Set `'iconauth.backend.IconAuthBackend'` as your authentication backend `AUTHENTICATION_BACKENDS = [ 'iconauth.backend.IconAuthBackend' ]`
3. Bind a url to `iconauth.views.login_view`


## Demo
1. `pip install https://github.com/ReliantNode/django-icon-auth/archive/master.zip`
2. `git clone https://github.com/ReliantNode/django-icon-auth`
3. `cd django-icon-auth/iconauth_demo/`
4. `python3 manage.py migrate`
5. `python3 manage.py runserver`
