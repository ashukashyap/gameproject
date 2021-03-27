from django.shortcuts import render
from .models import Post,Rahul,Table,Contact,Singup,Record,blog
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.



def home(request):
    sager = Post.objects.all()
    ren = Rahul.objects.all()
    tab = Table.objects.all()
    sonu = Record.objects.all()
    deep = blog.objects.all()

    if request.method =="POST":
        email = request.POST['email']
        new_singup = Singup()
        new_singup.email = email
        new_singup.save()

    context = {
        'sug': sager,
        'mu': ren,
        'read':tab,
        'pol' :sonu,
        'sag':deep,

    }
    return render(request,'index.html',context)




def contact(request):
    
    if request.method =="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        

        if len(phone)<10:
            messages.error(request, 'Plese fill the form Correctly.!')

        else:
            contact = Contact(name=name,email=email,phone=phone,desc=desc)
            contact.save()
            messages.success(request, 'Your message has been Sand.!')

        

    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')


def terms(request):
    return render(request,'terms.html')


def desclimer(request):
    return render(request,'desclimer.html')  


def police(request):
    return render(request,'privic.html')   


def authorized_digital_sellers_view(request):
    return HttpResponse('google.com, pub-4911980105395655, DIRECT, f08c47fec0942fa0')        


