from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Category, Product
from django.shortcuts import render, redirect, get_object_or_404  

# Create your views here.
def contact(request):
    categories = Category.objects.all()
    return render(request, 'app/contact.html',{'categories': categories})
#detail (chi tiết)
def detail(request):
    if request.user.is_authenticated:
        # Lấy khách hàng dựa trên người dùng đã đăng nhập
        customer = request.user
        # Tìm hoặc tạo mới đơn hàng chưa hoàn thành
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # Lấy tất cả các OrderItem liên quan đến đơn hàng
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        # Tính tổng giá trị từng sản phẩm trong giỏ hàng
        for item in items:
            if item.product: # Kiểm tra item.product có phải None không
                item.total_price = item.product.price * item.quantity
            else:
                print(f"OrderItem ID: {item.id}, Product: {item.product}") # In ra log nếu là None
                # Xóa item khỏi giỏ hàng (nếu muốn)
                item.delete()
    else:
        items = []  # Nếu chưa đăng nhập, giỏ hàng rỗng
        order = {'get_cart_items': 0, 'get_cart_total': 0}  # Đơn hàng chưa có sản phẩm
        cartItems = order['get_cart_items']
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub =False)
    context = {'products':products,'categories':categories,'items': items, 'order': order,'cartItems':cartItems}  # Truyền dữ liệu giỏ hàng vào template
    return render(request, 'app/detail.html', context)

#homeview category(phan loai):
def category(request):
    categories = Category.objects.filter(is_sub=False)
    active_category_slug = request.GET.get('category', '')
    products = []  # Khởi tạo products là list rỗng
    active_category = None # Khởi tạo active_category
    if active_category_slug:
        active_category = get_object_or_404(Category, slug=active_category_slug) # Lấy category theo slug, trả về 404 nếu không tìm thấy
        products = Product.objects.filter(category=active_category) # Filter theo ForeignKey
    if request.user.is_authenticated:
      customer = request.user
      order, created = Order.objects.get_or_create(customer=customer, complete=False)
      items = order.orderitem_set.all()
      cartItems = order.get_cart_items
    else:
      cartItems = 0

    context = {
        'categories': categories,
        'products': products,
        'active_category': active_category, # Truyền category đã tìm được, hoặc None nếu không có slug
        'cartItems':cartItems,
    }
    return render(request, 'app/category.html', context) 

#homeview search:
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []  # Nếu chưa đăng nhập, giỏ hàng rỗng
        order = {'get_cart_items': 0, 'get_cart_total': 0}  # Đơn hàng chưa có sản phẩm
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    # Lấy tất cả sản phẩm từ database
    products = Product.objects.all()
    return render(request,'app/search.html',{'categories':categories,"searched":searched,"keys":keys,'products': products,'cartItems':cartItems})
#homeview đăng ký tài khoản
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request,'app/register.html',context)

#homeview đăng nhập tài khoản
def loginPage(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username =username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'Tên đăng nhập hoặc mật khẩu không đúng!')
    

    context = {}
    return render(request,'app/login.html',context)
def logoutPage(request):
    logout(request)
    return redirect('login')

#homeview trang chu
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
         cartItems = 0
    categories = Category.objects.filter(is_sub =False)
    #active_category = request.Get.get('category','')
    # Lấy tất cả sản phẩm từ database
    products = Product.objects.all()
    context = {'categories':categories,'products': products, 'cartItems':cartItems}  # Truyền dữ liệu sản phẩm vào template
    return render(request, 'app/home.html', context)

# Giỏ hàng view, hiển thị giỏ hàng của người dùng
def cart(request):
    if request.user.is_authenticated:
        # Lấy khách hàng dựa trên người dùng đã đăng nhập
        customer = request.user
        # Tìm hoặc tạo mới đơn hàng chưa hoàn thành
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        # Lấy tất cả các OrderItem liên quan đến đơn hàng
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        # Tính tổng giá trị từng sản phẩm trong giỏ hàng
        for item in items:
            if item.product: # Kiểm tra item.product có phải None không
                item.total_price = item.product.price * item.quantity
            else:
                print(f"OrderItem ID: {item.id}, Product: {item.product}") # In ra log nếu là None
                # Xóa item khỏi giỏ hàng (nếu muốn)
                item.delete()
    else:
        items = []  # Nếu chưa đăng nhập, giỏ hàng rỗng
        order = {'get_cart_items': 0, 'get_cart_total': 0}  # Đơn hàng chưa có sản phẩm
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    context = {'categories':categories,'items': items, 'order': order,'cartItems':cartItems}  # Truyền dữ liệu giỏ hàng vào template
    return render(request, 'app/cart.html', context)

# Checkout view, hiển thị trang thanh toán
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []  # Nếu chưa đăng nhập, giỏ hàng rỗng
        order = {'get_cart_items': 0, 'get_cart_total': 0}  # Đơn hàng chưa có sản phẩm
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    context = {'categories':categories,'items': items, 'order': order,'cartItems':cartItems}  # Truyền dữ liệu giỏ hàng vào template
    return render(request, 'app/checkout.html', context)

# Cập nhật số lượng sản phẩm trong giỏ hàng qua AJAX
@csrf_exempt  # Bỏ qua CSRF protection để API có thể nhận request từ client-side
def updateItem(request):
    if request.method == 'POST':
        try:
            # Parse dữ liệu JSON từ request body
            data = json.loads(request.body)
            product_id = data.get('productId')  # Lấy ID sản phẩm
            action = data.get('action')  # Lấy action (add hoặc remove)

            # Lấy OrderItem dựa trên product_id
            order_item = OrderItem.objects.get(product__id=product_id)

            # Thực hiện hành động theo yêu cầu (add hoặc remove)
            if action == 'add':
                order_item.quantity = order_item.quantity + 1  # Thêm sản phẩm vào giỏ hàng
            elif action == 'remove':
                order_item.quantity = order_item.quantity - 1  # Giảm số lượng sản phẩm trong giỏ

            # Lưu thay đổi vào cơ sở dữ liệu
            order_item.save()

            # Trả về kết quả thành công
            return JsonResponse({'message': 'Cập nhật thành công!'}, status=200)

        except Exception as e:
            # Trả về lỗi nếu có sự cố
            return JsonResponse({'error': str(e)}, status=500)

    # Nếu không phải POST request, trả về lỗi
    return JsonResponse({'error': 'Invalid request'}, status=400)
