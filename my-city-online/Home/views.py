from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .models import *
from .forms import ContactForm
import smtplib
from email.message import EmailMessage


# Create your views here.


def search(request):
    name=request.GET.get('search')
    C=Category.objects.filter(Cname=name)
    
    if C :
        context={
            'item':C
        }
        return render(request,'base.html',context)
    else:
        return HttpResponse('not available')    


def contact(request):

    if request.method=='POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['your_name']
            email=form.cleaned_data['your_email']
            mobile=form.cleaned_data['mobile_number']
            city=form.cleaned_data['your_city']
            c= ContactUs(Name=name,Email=email,Mobile=mobile,City=city)
            c.save()
            return render(request,'contactdetails.html')
        else:
            return HttpResponse('form data is not valid')    

    else:
        form=ContactForm()
            

    return render(request, 'contact.html',{'form':form})

   


def index(request):
    C=Category.objects.all()
    B= Category.objects.count()/4
    context={
        "C":C,'B':B
    }
    return render(request,'index.html',context)

def newc(request):
    if request.method=='POST':
        cname=request.POST.get('inputName')
        name=request.POST.get('inputNamey')
        mobile=request.POST.get('inputMobile')
        city=request.POST.get('inputCity')

        content=f'''Hi Sir,
                   You have a suggestion to add new Category in your AnyPlace Project by Mr./Ms. {name} from {city}  and the category name is  "{cname}"'''
        sub='Add New Category'
        to='tsss.1920@gmail.com'

        msg=EmailMessage()
        msg.set_content(content)
        msg['subject']=sub
        msg['to']=to
        msg['from']='18bit053@ietdavv.edu.in'

        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login('18bit053@ietdavv.edu.in','S@ur@bh1998')
        s.send_message(msg)
        messages.success(request,f"We have received your Suggestion to Add {cname} as New Category, Thank you.")
        return render(request,'index.html')

    else:
         return render(request,'newc.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    try:

        if request.method=='POST':
            username1=request.POST.get('InputUsername')
            password1=request.POST.get('InputPassword')
            email1=request.POST.get('InputEmail')
            r=User.objects.create_user(username1,email1,password1)
            r.save()
            messages.success(request,'Congrets! Registered Successfully.')
            return render(request,'index.html')
        return redirect('/')    
      
         

    except Exception as e:
        return redirect('/')  

          
         



def loginuser(request):
    if request.method=='POST':
        username=  request.POST.get("InputUsername1")
        password=  request.POST.get("InputPassword1")
        user=      authenticate(username=username,password=password)
        if user is not None :
            login(request,user)
            messages.success(request,'Congrets! You have Logged in Successfully.')
            return render(request,'index.html') 
           
        else:
            return HttpResponse('not an authorised user')     


    return redirect('/')           


        
    
def logoutuser(request):
    logout(request)
    return render(request,'index.html')

def categories(request):
    C=Category.objects.all()
    context={
        'C':C
    }


    return render(request,'categories.html',context)

def register(request):
    if request.method=='POST':
        category=request.POST.get('InputCategory')
        name=request.POST.get('InputName')
        mobile=request.POST.get('InputMobile')
        address =request.POST.get('InputAddress')
        image=request.FILES.get('InputImage')
        if category=='Advocates':
            a=Advocates(name=name,mobile=mobile,Address=address,image=image)
            a.save()
        elif category=='Astrologers':
            a=Astrologers(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='AutomobileRepair':
            a=AutomobileRepair(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Bakeries':
            a=Bakeries(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Banks':
            a= Banks(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Books_Stationaries':
            a=Books_Stationaries(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Builders':
            a=Builders(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='CA':
            a=CA(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Carpenters':
            a=Carpenters(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Cloths':
            a=Cloths(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Computers':
            a=Computers(name=name,mobile=mobile,Address=address)
            a.save()   
        elif category=='Catering':
            a=Catering(name=name,mobile=mobile,Address=address)
            a.save()        
        elif category=='Courier':
            a=Courier(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Doctors':
            a=Doctors(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category==' Drivers':
            a= Drivers(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='DryCleaners':
            a=DryCleaners(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Electricians':
            a=Electricians(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Electronics':
            a=Electronics(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='EventManagement':
            a=EventManagement(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='FastFood':
            a=FastFood(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Footwear':
            a=Footwear(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Furniture':
            a=Furniture(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='GasAgencies':
            a=GasAgencies(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='GiftShops':
            a=GiftShops(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Gyms':
            a=Gyms(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='HairSaloon':
            a=HairSaloon(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Hotels':
            a=Hotels(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Jwellery':
            a=Jwellery(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='KiranaGeneral':
            a=KiranaGeneral(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Labours':
            a=Labours(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Medical':
            a=Medical(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Tiffin':
            a=Tiffin(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Milk':
            a=Milk(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='News':
            a=News(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Opticals':
            a=Opticals(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='PetrolPump':
            a=PetrolPump(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='PStudio':
            a=PStudio(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Plumber':
            a=Plumber(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='PropertyDealer':
            a=PropertyDealer(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Restaurant':
            a=Restaurant(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='School':
            a=School(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Tailor':
            a=Tailor(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='TentHouse':
            a=TentHouse(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='Transport':
            a=Transport(name=name,mobile=mobile,Address=address)
            a.save() 
        elif category=='WaterRO':
            a=WaterRO(name=name,mobile=mobile,Address=address)
            a.save() 

        return redirect('/')        
def addBussiness(request):
    return render(request,'add_bussiness.html')


def adv(request):
     a=Advocates.objects.all()
     return render(request,'category/adv.html',{'a':a})

def ast(request):
     a=Astrologers.objects.all()
     return render(request,'category/ast.html',{'a':a}) 

def aut(request):
     a=AutomobileRepair.objects.all()
     return render(request,'category/aut.html',{'a':a}) 

def bkr(request):
     a=Bakeries.objects.all()
     return render(request,'category/bkr.html',{'a':a})    

def bnk(request):
     a=Banks.objects.all()
     return render(request,'category/bnk.html',{'a':a})

def books(request):
     a=Books_Stationaries.objects.all()
     return render(request,'category/books.html',{'a':a})

def bldr(request):
     a=Builders.objects.all()
     return render(request,'category/bldr.html',{'a':a})

def ca(request):
     a=CA.objects.all()
     return render(request,'category/ca.html',{'a':a})

def carp(request):
     a=Carpenters.objects.all()
     return render(request,'category/carp.html',{'a':a})

def clth(request):
     a=Cloths.objects.all()
     return render(request,'category/clth.html',{'a':a})

def cmputr(request):
     a=Computers.objects.all()
     return render(request,'category/cmputr.html',{'a':a})

def ctring(request):
     a=Catering.objects.all()
     return render(request,'category/ctring.html',{'a':a})

def cr(request):
     a=Courier.objects.all()
     return render(request,'category/cr.html',{'a':a}) 

def dct(request):
     a=Doctors.objects.all()
     return render(request,'category/dct.html',{'a':a}) 

def drv(request):
     a=Drivers.objects.all()
     return render(request,'category/drv.html',{'a':a})

def dry(request):
     a=DryCleaners.objects.all()
     return render(request,'category/dry.html',{'a':a})

def elect(request):
     a=Electricians.objects.all()
     return render(request,'category/elect.html',{'a':a})

def electr(request):
     a=Electronics.objects.all()
     return render(request,'category/electr.html',{'a':a})

def em(request):
     a=EventaManagement.objects.all()
     return render(request,'category/em.html',{'a':a})

def ff(request):
     a=FastFood.objects.all()
     return render(request,'category/ff.html',{'a':a})

def fw(request):
     a=Footwear.objects.all()
     return render(request,'category/fw.html',{'a':a})

def fn(request):
     a=Furniture.objects.all()
     return render(request,'category/fn.html',{'a':a})

def ga(request):
     a=GasAgencies.objects.all()
     return render(request,'category/ga.html',{'a':a})

def gs(request):
     a=GiftShops.objects.all()
     return render(request,'category/.html',{'a':a})

def gm(request):
     a=Gyms.objects.all()
     return render(request,'category/gm.html',{'a':a})

def hs(request):
     a=HairSaloon.objects.all()
     return render(request,'category/hs.html',{'a':a})

def hotel(request):
     a=Hotels.objects.all()
     return render(request,'category/hotel.html',{'a':a})

def js(request):
     a=Jwellery.objects.all()
     return render(request,'category/js.html',{'a':a})

def k_g(request):
     a=KiranaGeneral.objects.all()
     return render(request,'category/k&g.html',{'a':a})

def lb(request):
     a=Labours.objects.all()
     return render(request,'category/lb.html',{'a':a})

def mdc(request):
     a=Medical.objects.all()
     return render(request,'category/mdc.html',{'a':a})

def md(request):
     a=Milk.objects.all()
     return render(request,'category/md.html',{'a':a})

def nws(request):
     a=News.objects.all()
     return render(request,'category/nws.html',{'a':a})

def opt(request):
     a=Opticals.objects.all()
     return render(request,'category/opt.html',{'a':a})

def pp(request):
     a=PetrolPump.objects.all()
     return render(request,'category/pp.html',{'a':a})

def ps(request):
     a=PStudio.objects.all()
     return render(request,'category/ps.html',{'a':a})

def pl(request):
     a=Plumber.objects.all()
     return render(request,'category/pl.html',{'a':a})

def pd(request):
     a=PropertyDealer.objects.all()
     return render(request,'category/pd.html',{'a':a})

def rst(request):
     a=Restaurant.objects.all()
     return render(request,'category/rst.html',{'a':a})

def sch(request):
     a=School.objects.all()
     return render(request,'category/sch.html',{'a':a})

def tl(request):
     a=Tailor.objects.all()
     return render(request,'category/tl.html',{'a':a})

def thd(request):
     a=TentHouse.objects.all()
     return render(request,'category/thd.html',{'a':a})

def tf(request):
     a=Tiffin.objects.all()
     return render(request,'category/tf.html',{'a':a})

def trn(request):
     a=Transport.objects.all()
     return render(request,'category/trn.html',{'a':a})

def row(request):
     a=WaterRO.objects.all()
     return render(request,'category/row.html',{'a':a})


        
            