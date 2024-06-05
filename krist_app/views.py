from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import randint
from django.shortcuts import render
import smtplib
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import hashlib




def indexpage(request):
    data = products.objects.all()
    
    return render(request,"app/index.html",{'product':data})
def homepage(request):
    return render(request,"app/home.html")

    


def registrpage(request):
    return render(request,"app/signin.html")

def Login(request):
    return render(request,"app/login.html")
def forgotpassword(request):
    return render(request,"app/ForgotPassword.html")


def UserRegister(request):
    if request.method == "POST":
        Username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        rpassword = request.POST['rpassword']
        
        user = userAccount.objects.filter(Email=email)
        
        if user:
            message = "User Alreadt exist"
            return render(request,"app/login.html",{'msg':message})
        else:
            if password == rpassword:
                hashed_password = hashlib.sha256(password.encode()).hexdigest()

                newUser = userAccount.objects.create(Name=Username,Email=email,Password=hashed_password)
                message = "Registerd Successfully"
                return render(request,"app/login.html",{'msg':message})
            else:
                message = "Password and Confirm password does not match"
                return render(request,"app/signin.html",{'msg':message})
                
        
def LoginUser(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = userAccount.objects.get(Email=email)
            data = products.objects.all()

            hashed_password = hashlib.sha256(password.encode()).hexdigest()

            if user.Password == hashed_password:
                request.session['Name'] = user.Name
                return render(request, "app/home.html", {'key1': data})
            else:
                message = "Username and Password Do not match"
                return render(request, "app/login.html", {'msg': message})
        
        except ObjectDoesNotExist:
            message = "User does not exist"
            return render(request, "app/login.html", {'msg': message})
        
def logout(request):
    return redirect("index")

def forgotpage(request):
    if request.method == "POST":
        mail = request.POST['email']
        user = userAccount.objects.filter(Email=mail)
        
        if user:
            request.session['Email'] = mail
            otp = randint(1000,9999)
            newotp = UserOtp.objects.create(Email=mail,otp=otp)
            s = smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login('bhatthappy02@gmail.com','ilao yplb vsve etbb')
            message = f'Subject: Your One Time Password\n\nYour One Time Password is: {otp}'
            s.sendmail('bhatthappy02@gmail.com',mail,message)
            s.quit()
      
            return render(request,"app/otp.html")
        else:
            message = "Email Not Found"
            return render(request,"app/ForgotPassword.html",{'msg':message})
        
        
def otpverify(request):
    if request.method == "POST":
        num = request.POST['otp']
        otp = UserOtp.objects.get(otp=num)
        
        if otp:
            return render(request,"app/resetpassword.html")
        else:
            message = "Otp Is Incorrect"
            return render(request,"app/otp.html",{'msg':message})
        
def updatapassword(request):
    if request.method == "POST":
        password = request.POST['password']
        cpassword = request.POST['confirmPassword']

        if password == cpassword:
            em = request.POST['email']
            user = userAccount.objects.get(Email=em)

            if user:
                hased_password = hashlib.sha256(cpassword.encode()).hexdigest()
                user.Password = hased_password
                user.save()
                messages.success(request, "Password Change Successfully")
                return render(request,"app/login.html")
            else:
                message = "USer Not Found"
                return render(request,"app/resetpassword.html",{'msg':message})
        else:
            message = "Passoword and confirm password not match"
            return render(request,"app/resetpassword.html",{'msg':message})
        
def add_to_cart_or_redirect(request, product_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            product = products.objects.get(pk=product_id)
            

            messages.success(request, "Item added to cart successfully.")
            return redirect("cartadd") 
    else:
        
        messages.warning(request, "Please login to add items to cart.")
        return redirect("loginpage")  
    
def product_detail(request, product_id):
    product = products.objects.get(pk=product_id)
    return render(request, "app/single_product.html", {'product': product})
    

def add_to_cart(request, product_id):
    if request.method == "POST" and 'remove_item_id' in request.POST:
       
        remove_item_id = request.POST.get('remove_item_id')
        cart_item = cart.objects.filter(pk=remove_item_id).first()  # Get the cart item
        if cart_item:
            cart_item.delete()  
            return redirect('cartadd')  

    
    product = products.objects.get(pk=product_id)
    name = product.productname
    price = product.productprice
    image = product.productimage.url
    cart_item = cart.objects.create(name=name, price=price, image=image)

    total_count = cart.objects.count()

    return render(request, "app/add_cart.html", {'product': product, 'total': total_count})

def removecart(request):
    return redirect('home')
    






def placeorder(request, product_id):
   
        product = products.objects.get(pk=product_id)
        
        request.session['pname'] = product.productname
        request.session['pprice'] = str(product.productprice)
        request.session['qty'] = request.POST['quantity']
        
        
        
        
        return render(request, "app/place_order.html",{'product':product}) 
   

def makeorder(request):
    if request.method == "POST":
        user_name = request.POST['name']
        address = request.POST['address']
        mobile = request.POST['contactno']
        pname = request.session.get('pname')
        pprice = request.session.get('pprice')
        pqty = request.session.get('qty')
        make_order = order.objects.create(user_name=user_name,user_address=address,user_moblieno=mobile,product_name=pname,product_price=pprice,product_qty=pqty)
        return redirect('home')




   
    
   
    
    
    
    
            
                 
        
#######  Admin Side #######
            
    

def adminpage(request):
    return render(request,"app/admin/login.html")
def adminindex(request):
    return render(request,"app/admin/index.html")

def adminlogin(request):
    username = request.POST['uname']
    password = request.POST['password']
    
    user = admin.objects.filter(username=username,password=password)
    
    if user: 
        return render(request,"app/admin/index.html")
    else:
        message = "username and password does not match"
        return render(request,"app/admin/login.html",{'msg':message})

def addprod(request):
    return render(request,"app/admin/addProducts.html")

def addproduct(request):
    if request.method == "POST":
        
        pid = request.POST['pid']
        pname = request.POST['pname']
        pcategory = request.POST['pcategory']
        pprice = request.POST['pprice']
        pdesc = request.POST['pdesc']
        pimage = request.FILES['pimage']
        
        user = products.objects.create(product_id=pid,productname=pname,productcategory=pcategory,productprice=pprice,productdescription=pdesc,productimage=pimage)
        
        if user:
            message = "Product Add Successfully"
            return render(request,"app/admin/addProducts.html",{'msg':message})
        else:
            text = "Error To Add Product"
            return render(request,"app/admin/addProducts.html",{'text':text})

def displayproduct(request):
    data = products.objects.all()
    return render(request,"app/admin/products.html",{'key1':data})

def removeproduct(request):
    data = products.objects.all()
    return render(request,"app/admin/removeproduct.html",{'key1':data})

def user_list(request):
    data = userAccount.objects.all()
    return render(request,"app/admin/userlist.html",{'user':data})

def remove_user(request,id):
    user = userAccount.objects.get(pk=id)
    user.delete()
    return redirect('listuser')

def remove_product(request,product_id):
    product = products.objects.get(product_id=product_id)
    product.delete()
    return redirect('removeproduct')

def updateproduct(request):
    data = products.objects.all()
    return render(request,"app/admin/updateproduct.html",{'product':data})

def productupdate_process(request,product_id):
    product = products.objects.get(product_id=product_id)
    return render(request,"app/admin/update_product_form.html",{'data':product})

def update_product(request,product_id):
    product = products.objects.get(product_id=product_id)
    
    if product:
        product.productname = request.POST['product-name']
        product.productdescription = request.POST['product-description']
        product.productprice = request.POST['product-price']
        
        if "product-image" in request.FILES:
            product.productimage = request.FILES["product-image"]

        
        product.save()
        return redirect("productupdate")


def orderlist(request):
    data = order.objects.all()
    return render(request,'app/admin/orderlist.html',{'order':data})
    