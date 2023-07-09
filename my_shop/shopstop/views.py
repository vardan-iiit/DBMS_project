from django.shortcuts import render,redirect
from django.http import HttpResponse
from shopstop.forms import addcartform,loginform,cartform,placeorderform
from .models import Customer,Product,Cart,InCartProducts,ShippingAddress,Orders
from datetime import datetime,date
# Create your views here.

def index(request):
    
    try:
        if request.method == 'POST':

                form = loginform(request.POST)
                
              
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                email = request.POST['email']
                custid=int(request.POST['custid'])

                if Customer.objects.filter(pk=custid).exists():
                    print("customer exists")
                    pass
                else:
                    newcust=Customer()
                    newcust.customer_id=custid
                    newcust.first_name=firstname
                    newcust.last_name=lastname
                    newcust.email_address=email
                    newcust.date_of_creation=None
                    newcust.last_login=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    
                    try:
                        newcust.save()  
                    except Exception as e:
                        print(f"Error saving customer: {e}")
                    

                products = Product.objects.all()
    
                return render(request, 'shopstop/product.html', {'products': products})
                
                
               
                
        else:
            form = loginform()
    except:
        pass
    return render(request,'shopstop/index.html')

def about(request):
    return HttpResponse('about')

def contact(request):
    return HttpResponse('contact')

def tracker(request):
    return HttpResponse('tracker')

def search(request):
    return HttpResponse('search')

def proview(request):
    products = Product.objects.all()
    
    return render(request, 'shopstop/product.html', {'products': products})
    

def checkout(request):
    return HttpResponse('checkout')


def placeorder(request):
    try:
        if request.method == 'POST':
                
                form = placeorderform(request.POST)
                name=request.POST['name']
                phone=int(request.POST['phone'])
                city=request.POST['city']
                state=request.POST['state']
                country=request.POST['country']
                postal=request.POST['postal']
                userid=int(request.POST['custid'])
                
                
                if Customer.objects.filter(pk=userid).exists():
                    
                    shipp=ShippingAddress()
                    shipp.shipping_id=int(ShippingAddress.objects.latest("shipping_id").shipping_id)+1
                    shipp.reciever_name=name
                    shipp.receiver_phonenumber=phone
                    shipp.city=city
                    shipp.state=state
                    shipp.country=country
                    shipp.postal_code=postal
                    shipp.cust=Customer.objects.get(pk=userid)
                    
                    
                                    
                    try:
                        shipp.save()
                        orderobj=Orders()
                        orderobj.order_id=int(Orders.objects.latest("order_id").order_id)+1
                        orderobj.cart=Cart.objects.get(cust=userid)
                        orderobj.payable_amount=Cart.objects.get(cust=userid).cart_amount
                        orderobj.stats="Pending"
                        orderobj.save()
                        context = {
                            'user': userid,
                            'amount': orderobj.payable_amount
                        }

                        return render(request, 'shopstop/checkout.html',context)
                        
                    except Exception as e:
                        print(e)
                else:
                    print("customer doesnt exists")
                    pass
                   
        else:
            form = placeorderform()
    except:
        pass
    
    return render(request, 'shopstop/orders.html')

def addtocart(request):
    try:
        if request.method == 'POST':

                form = addcartform(request.POST)
                
              
                userid = int(request.POST['userid'])
                productname = request.POST['productname']
                quantity = int(request.POST['quantity'])
                
                

                if Customer.objects.filter(pk=userid).exists():
                    try:
                        
                        if Cart.objects.filter(cust=userid).exists():
                            
                            newcart=Cart.objects.filter(cust=userid)
                            newincart=InCartProducts()
                            newincart.incart_id=int(InCartProducts.objects.latest("incart_id").incart_id)+1
                            
                        else:
                            
                            newcart=Cart()
                            newcart.cart_id=int(Cart.objects.latest("cart_id").cart_id)+1
                            newcart.cust=Customer.objects.get(pk=userid)
                            newcart.cart_amount=0
                            
                            newincart=InCartProducts()

                            newincart.incart_id=int(InCartProducts.objects.latest("incart_id").incart_id)+1
                      
                    except Exception as e:
                        print(e)
                    
                    
                    
                    
                    
                    
                    
                    if Product.objects.filter(product_name=productname).exists():
                        
                        newincart.quantity_of_products=quantity
                        newincart.pro=Product.objects.get(product_name=productname)
                        newcart.cart_amount+=newincart.pro.product_price*quantity
                        try:
                            newcart.save()  
                            
                        except Exception as e:
                            print(f"Error saving customer cart: {e}")

                        try:
                            newincart.cart=Cart.objects.get(pk=newcart.cart_id)
                            newincart.save()  
                        except Exception as e:
                            print(f"Error saving customer incart: {e}")   
                        
                    else:
                        print("product doesnt exists")
                    
                    

                    

                else:
               
                   
                    return render(request,'shopstop/index.html')
                
                    
                    
                    
                products = Product.objects.all()
    
                return render(request, 'shopstop/product.html', {'products': products})   
                   

                
                
                
                
                
        else:
            form = addcartform()
    except:
        pass
    return render(request,'shopstop/cart.html')


def viewcart(request):
         
    try:
        if request.method == 'POST':
                
                form = cartform(request.POST)
                
                userid=int(request.POST['userid'])
                
                
                if Customer.objects.filter(pk=userid).exists():
                    try:
                        
                        custcart=Cart.objects.filter(cust=userid)
                        for obj in custcart:
                            
                            products= InCartProducts.objects.filter(cart=obj.cart_id)
                    except Exception as e:
                        print(e)
                      
                    try:
                        return render(request, 'shopstop/viewcart2.html', {'products': products})
                    except Exception as e:
                        print(e)
                else:
                    print("customer doesnt exists")
                    pass
                   
        else:
            form = cartform()
    except:
        pass
    return render(request,"shopstop/viewcart.html")
