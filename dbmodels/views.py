from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from .models import Login,ALogin,User

  

def user_login(request):
    return render(request, 'user_login.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Login.loginauth_objects.get(username=username,password=password)
            if user is not None:
                query_res = User.objects.filter(username=username).values()
                template = loader.get_template('Dashboard.html')
                context = {
                    'mymembers': query_res,
                }
                return HttpResponse(template.render(context, request))
                #return render(request,'Dashboard.html',{})
            else:
                return redirect('/')
        except Exception as Identifier:
            return redirect('/')

    else:
        return render(request, 'user_login.html')
  

def admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=ALogin.loginauth_objects.get(username=username,password=password)
            if user is not None:
                query_res = User.objects.all()
                return render(request,'admin_dash.html',{'query_res':query_res})
            else:
                print("Incorrect Combination of username and password")
                return redirect('/')
        except Exception as Identifier:
            return redirect('/')

    else:
        return render(request, 'user_login.html')