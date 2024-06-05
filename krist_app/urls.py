from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    
    path("",views.indexpage,name="index"),
    path("pagehome",views.homepage,name="home"),
    path("registerpage/",views.registrpage,name="registerpage"),
    path("register/",views.UserRegister,name="userrgister"),
    path("forgotpassword/",views.forgotpassword,name="forgotP"),
    path("otppage",views.forgotpage,name="forgotpage"),
    path("login/",views.LoginUser,name="loginuser"),
    path("loginpage/",views.Login,name="loginpage"),
    path("productdisp/",views.displayproduct,name="displayproduct"),
    path("verifyotp/",views.otpverify,name="otpverify"),
    path("resetp/",views.updatapassword,name="resetpassword"),
    path("logout/",views.logout,name="logout"),
    path("check_user/<int:product_id>",views.add_to_cart_or_redirect,name="user_check"),
    path('detailproduct/<int:product_id>',views.product_detail, name='productdetail'),
    path('addcart/<int:product_id>',views.add_to_cart,name="cartadd"),
    path('reomovecart/',views.removecart,name="cartremove"),
    path('placeorder/<int:product_id>',views.placeorder,name="order"),
    path('makeorder',views.makeorder,name="ordermake"),
    
    
    
    ## Admin Side ##
    path("adminpage/",views.adminpage,name="adminpage"),
    path("adminindex/",views.adminindex,name="indexadmin"),
    path("adminlogin/",views.adminlogin,name="login"),
    path("addProd/",views.addprod,name="addproducts"),
    path("addProduct/",views.addproduct,name="addproduct"),
    path("deleteproduct/",views.removeproduct,name="removeproduct"),
    path("userlist/",views.user_list,name="listuser"),
    path("removeuser/<int:id>",views.remove_user,name="userdelet"),
    path("removeproduct/<int:product_id>",views.remove_product,name="productremove"),
    path("update/",views.updateproduct,name="productupdate"),
    path("product_update/<int:product_id>",views.productupdate_process,name="product_update"),
    path("prodcut_update/<int:product_id>",views.update_product,name="update_product"),
    path("orderlist/",views.orderlist,name="listorder")
    
    

]