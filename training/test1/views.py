from django.http import HttpResponse
from django.shortcuts import render
from.models import Person

# Create your views here.
def home(request):
    return render(request,'head.html')
def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def product(request):
    return render(request,'product.html')
def service(request):
    return render(request,'show.html')
def prog(request):
    return render(request,'prog.html')
def mypage(request):
    if request.method=="POST":
        fn=request.POST.get('fn')
        sn=request.POST.get('ln')
        print(fn,"-----",sn)
        res=Person(first_name=fn,last_name=sn)
        res.save()
    return render(request,'mypage.html')


def show(request):
    data=Person.objects.all()
    diss={'data':data}
    print(data)
    return render(request,'show.html',diss)









