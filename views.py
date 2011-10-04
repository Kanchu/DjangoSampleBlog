from django.shortcuts import render_to_response
from django.views.generic.create_update import create_object, delete_object
from django.core.urlresolvers import reverse
from models import Blog
import re

def index(request):
	return render_to_response('index.html')

def home(request):
	return render_to_response('home.html')

def add(request):
    try:
        var1 = request.GET['var1']
        var2 = request.GET['var2']
        opr = request.GET['opr']
        if re.match("\d+",var1):
            no1 = int(var1)
            no2 = int(var2)
            flag = 1
            if opr=='add':
                res =  no1+no2
            else:
                res = no1-no2

        else:
            res = "Invalid Input Numbers!!!"
            flag = 0
        return render_to_response('add.html',{
            "res" : res,
            "num1": var1,
            "num2": var2,
            "flag": flag,
            "opr": opr
        })
    except :
       return render_to_response('home.html')

def feedback(request):

    return create_object(request,
        model=Blog,
        template_name='feedback.html',
        post_save_redirect="list_feedback"
    )


def list_feedback(request):
    queryset=Blog.objects.all()
    return render_to_response("list_feedback.html",{
        "list_feed" : queryset
    })

def detail(request, id):
    obj = Blog.objects.all()
    id1 = int(id)
    return render_to_response("detail.html",{
        "obj" : obj,
        "id1" : id1
    })

def del_feed(request,id):
    queryset=Blog.objects.all()
    for i in queryset:
        if i.id==int(id):
            i.delete()

    return render_to_response("list_feedback.html",{
        "list_feed" : Blog.objects.all()
    })
#
def delete(request,id):
#    queryset=Blog.objects.all()
#    for i in queryset:
#        if i.id==int(id):
#            i.delete()

    return render_to_response("delete.html",{
        "list_feed" : Blog.objects.all(),
        "id" : id
    })