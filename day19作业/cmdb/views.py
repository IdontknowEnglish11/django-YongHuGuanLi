from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

from cmdb import models
def login(request):
    if request.method=='GET':
        obj=models.UserGroup.objects.all()
        # for row in obj:
        #     # print(row.caption)
        return  render(request,'login.html',{'acption':obj})
    elif request.method=='POST':
        u=request.POST.get('username')
        p=request.POST.get('pwd')
        print(u,p)
        obj=models.UserInfo.objects.filter(username=u,password=p)

        if obj:
            obj = models.UserInfo.objects.all()
            return render(request, 'index.html', {'obj': obj})
        else:
            return HttpResponse('404')

def tang(request):

    u=request.POST.get('user')
    p=request.POST.get('password')
    e=request.POST.get('email')
    t=request.POST.get('title')
    print(u,p,e,t)
    obj=models.UserInfo.objects.filter(username=u).first()
    if obj:
        return HttpResponse('用户已存在')
    models.UserInfo.objects.create(username=u,password=p,email=e,user_group_id=t)

    return redirect('/login/')

def index(request):
    if request.method=='GET':
        return redirect('/login/')
    elif request.method=='POST':
        obj=models.UserInfo.objects.all()
        return  render(request,'index.html',{'obj':obj})

def detail(request,nid):
    obj = models.UserInfo.objects.all()
    group_obj = models.UserGroup.objects.all()
    return render(request,'detail.html',{'obj':obj,'group_obj':group_obj})

def edit(request):
    u=request.POST.get('user')
    p=request.POST.get('pwd')
    e=request.POST.get('email')
    t=request.POST.get('title')
    print(u,p,e,t)
    models.UserInfo.objects.update(username=u,password=p,email=e,user_group_id=t)
    return  redirect('/index/')

def dele(request,uid):
    models.UserInfo.objects.filter(id=uid).delete()
    return redirect('/index/')