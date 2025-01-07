from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

#Create your models here.
class MyForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.CharField()
#Cagtegory phân loại
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

#Thay đổi form đăng ký django
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
# Customer Model: Lưu thông tin khách hàng liên kết với User từ Django
# class Customer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)  # Liên kết với User
#     name = models.CharField(max_length=200, null=True)  # Tên khách hàng
#     email = models.CharField(max_length=200, null=True)  # Email của khách hàng

#     def __str__(self):
#         return self.name


# Product Model: Lưu thông tin sản phẩm bao gồm tên, giá, ảnh và trạng thái digital
class Product(models.Model):
    category = models.ManyToManyField(Category,related_name='product')
    name = models.CharField(max_length=200, null=True)  # Tên sản phẩm
    price = models.FloatField()  # Giá của sản phẩm
    digital = models.BooleanField(default=False, null=True, blank=False)  # Nếu là sản phẩm số
    image = models.ImageField(null=True, blank=True)  # Ảnh của sản phẩm
    detail = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    @property
    # Hàm trả về URL của ảnh sản phẩm
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# Order Model: Lưu thông tin đơn hàng bao gồm khách hàng, ngày đặt, trạng thái và mã giao dịch
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)  # Khách hàng liên kết
    date_order = models.DateTimeField(auto_now_add=True)  # Ngày đặt hàng
    name = models.CharField(max_length=200, null=True)  # Tên của đơn hàng
    complete = models.BooleanField(default=False, null=True, blank=False)  # Trạng thái đơn hàng
    transaction_id = models.CharField(max_length=200, null=True)  # Mã giao dịch

    def __str__(self):
        return str(self.id)
    
    @property
    # Đếm số lượng sản phẩm trong đơn hàng
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()  # Lấy tất cả các OrderItem trong đơn hàng
        total = sum([item.quantity for item in orderitems])  # Tổng số lượng sản phẩm
        return total
    
    @property
    # Tính tổng tiền của đơn hàng
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()  # Lấy tất cả các OrderItem trong đơn hàng
        total = sum([item.get_total for item in orderitems])  # Tổng tiền
        return total


# OrderItem Model: Lưu thông tin các sản phẩm trong một đơn hàng
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=False, null=True)  # Sản phẩm liên kết
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=False, null=True)  # Đơn hàng liên kết
    quantity = models.IntegerField(default=0, null=True, blank=True)  # Số lượng của sản phẩm
    date_added = models.DateTimeField(auto_now_add=True)  # Ngày thêm sản phẩm vào đơn hàng
    
    @property
    # Tính tổng tiền của một sản phẩm trong đơn hàng
    def get_total(self):
        total = self.product.price * self.quantity  # Giá * số lượng
        return total


# ShippingAddress Model: Lưu thông tin địa chỉ giao hàng cho đơn hàng
class ShippingAddress(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=False, null=True)  # Khách hàng liên kết
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=False, null=True)  # Đơn hàng liên kết
    quantity = models.IntegerField(default=0, null=True, blank=True)  # Số lượng (có thể không cần thiết)
    date_added = models.DateTimeField(auto_now_add=True)  # Ngày thêm địa chỉ
    address = models.CharField(max_length=200, null=True)  # Địa chỉ giao hàng
    city = models.CharField(max_length=200, null=True)  # Thành phố
    state = models.CharField(max_length=200, null=True)  # Tỉnh/Thành
    mobile = models.CharField(max_length=10, null=True)  # Số điện thoại

    def __str__(self):
        return self.address
