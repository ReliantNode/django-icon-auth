import random
import string

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.conf import settings


from iconauth.forms import LoginForm
from iconauth.utils import recover_to_addr


def login_view(request, template_name='iconauth/login.html'):


    if request.method == 'POST':
        token = request.session['login_token']
        form = LoginForm(token, request.POST)
        if form.is_valid():
            user = authenticate(request=request, address=form.data['username'], token=token, signature=form.data['signature'])
            if user is not None:
                del request.session['login_token']
                login(request, user)                
                return redirect(settings.LOGIN_REDIRECT_URL)

        form.add_error(None, "Failed Authentication - Try Again")

        return render(request, template_name, {'form' : form,'login_token' : token})

    else:
        zeros = '0' * 32
        token = ''.join(random.choice('0123456789abcdef') for n in range(32)) + zeros
        request.session['login_token'] = token
        form = LoginForm(token)
        
        return render(request, template_name, {'form' : form,'login_token' : token})

