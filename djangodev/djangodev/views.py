from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.base import RedirectView 

def index(request):
    html = """<h1>Data Flair Django</h1>Hello, you just configured your first URL"""
    return HttpResponse(html)

def data_flair(request):
    return redirect('/dataflair')

class tutorial(RedirectView): url = 'https://data-flair.training/blogs/category/django/' 
# url di atas adl atribut dari RedirectView and contains the value of a URL, 
# can take placeholders from Python, thus, your URLs can be more dynamic, maka url ini akan me-redirect kita
# ke page yg di isi dlm variable url tersebut, atau kita bisa juga dengan menggunakan langsung
# atribut url pada views. check views.py pada root 

# infinite redirect cycle
def inf1(request):
    return redirect('/inf2')

def inf2(request):
    return redirect('/inf1')

# mine sample, see this https://docs.djangoproject.com/en/3.0/intro/tutorial03/
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

#def setcookie(request):
#    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
#    html.set_cookie('dataflair', 'Hello this is your Cookies', max_age = None)
#    return html

## request.COOKIES
#def showcookie(request):
#    # django request object memiliki atribut COOKIES sprti COOKIES array pada PHP ($_COOKIE[])
#    # COOKIES adl atribut spesial dr object request
#    show = request.COOKIES['dataflair']
#    html = "<center> New Page <br> {0}</center>".format(show) # print Hello this is your Cookies
#    return HttpResponse(html)

# Using request.COOKIES.get(). Let's modifiy function setcookie above
def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        text = "Welcome Back"
        html.set_cookie('dataflair', text)
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = "Welcome for the first time"
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

# modify showcookie()
def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else:
        return redirect('/setcookie')
# delete_cookie()
def delete_cookie(request):
    if request.COOKIES.get('visits'):
       response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
       response.delete_cookie('visits')
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response