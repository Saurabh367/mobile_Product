from django.shortcuts import render,HttpResponse



def home(request):
    return render(request,'head.html')
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def product(request):
    return render(request,'product.html')
def service(request):
    return render(request,'show.html')
def prog(request):
    return render(request,'prog.html')
def mypage(request):
    data={
        "roll":"100",
        "name":"amit"
    }
    return render(request, 'mypage.html',data)




