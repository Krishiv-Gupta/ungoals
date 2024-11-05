from django.shortcuts import render,redirect
from .models import e,goal

# Create your views here.
def home(request):
    c=goal.objects.all()
    context={"c":c}
    return render(request,"base.html",context)

def send(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        w=request.POST['reason']

        b=e(Name=name,Email=email,Phone=phone,W=w)
        b.save()

        return redirect('home')
    return render(request,"base.html")

def play(request):
    return render(request,"game.html")



def volunteer(request):
    codes=e.objects.all()

    context={'c':codes}
    return render(request,"volunteers.html",context)


def search(request):
    if request.method=="POST":
        i=request.POST['s']
        c=goal.objects.filter(Name=i)
        if len(c)==0:
            return redirect('home')
        else:
            context={"o":c[0]}
            return render(request, "detail.html", context)

    return redirect('home')

def detail_1(request):
    o=goal.objects.filter(Name='No Poverty')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_2(request):
    o=goal.objects.filter(Name='Zero Hunger')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_3(request):
    o=goal.objects.filter(Name='Good Health And Well-Being')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_4(request):
    o=goal.objects.filter(Name='Quality Education')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_5(request):
    o=goal.objects.filter(Name='Gender Equality')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_6(request):
    o=goal.objects.filter(Name='Clean Water And Sanitation')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_7(request):
    o=goal.objects.filter(Name='Affordable And Clean Energy')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_8(request):
    o=goal.objects.filter(Name='Decent Work And Economic Growth')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_9(request):
    o=goal.objects.filter(Name='Industry, Innovation And Infrastructure')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_10(request):
    o=goal.objects.filter(Name='Reduced Inequalities')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_11(request):
    o=goal.objects.filter(Name='Sustainable Cities And Communities')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_12(request):
    o=goal.objects.filter(Name='Responsible Consumption And Production')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_13(request):
    o=goal.objects.filter(Name='Climate Action')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_14(request):
    o=goal.objects.filter(Name='Life Below Water')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_15(request):
    o=goal.objects.filter(Name='Life On Land')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_16(request):
    o=goal.objects.filter(Name='Peace, Justice And Strong Institutions')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)

def detail_17(request):
    o=goal.objects.filter(Name='Partnership For The Goals')
    
    context={"o":o[0]}
    return render(request, "detail.html", context)



