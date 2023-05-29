from django.shortcuts import render

# Create your views here.
def wish(request):
    d={'name':'Rahul','age':23,'course':'python'}
    return render(request,'wish.html',context=d)