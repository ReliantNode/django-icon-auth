from django.shortcuts import render, redirect
from django.conf import settings


# Create your views here.

def home(request):
	if request.user.is_anonymous:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	else:
		context = {}
		return render(request, "web/profile.html", context)