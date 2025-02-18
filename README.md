# GỬI LỜI TRÂN TRỌNG TỚI GIẢNG VIÊN NGUYỄN VĂN CHIẾN ĐÃ HỖ TRỢ CHÚNG EM TRONG SUỐT THỜI GIAN VỪA QUA

# **Hệ Thống Quản Lý Cửa Hàng Trang Sức**

## **Giới Thiệu**

Hệ thống quản lý cửa hàng trang sức là một nền tảng thương mại điện tử tiên tiến, được thiết kế để phục vụ cho ngành kinh doanh trang sức cao cấp. Hệ thống bao gồm hai thành phần chính

### **1. Trang Khách Hàng**
Trang dành cho khách hàng, nơi họ có thể duyệt sản phẩm, đặt hàng và thanh toán trực tuyến.

### **2. Trang Quản Lý**

Dành cho nhân viên và quản trị viên:
Quản lý quầy
Sản phẩm
Khuyến mãi
Mua lại
Nhân viên
Doanh thu
Khai báo
Tích điểm
Lịch sử mua hàng
Dashboard

---

## **Đặc Điểm Nổi Bật**

### **Công nghệ nền tảng:**

- **HTML**: Cung cấp giao diện người dùng và bố cục trình bày trực quan, dễ sử dụng.
- **Python**: Xử lý logic nghiệp vụ, quản lý dữ liệu và điều khiển phía backend.
- **CSS**: Tùy chỉnh giao diện và cải thiện trải nghiệm người dùng.
- **JavaScript**: Tạo hiệu ứng động và xử lý dữ liệu phía client, nâng cao tính tương tác.

---

## **Chức Năng Hệ Thống**

### **Trang Khách Hàng**

- **Quản lý danh mục sản phẩm**: Hiển thị danh mục với bộ lọc tìm kiếm nâng cao, giúp khách hàng dễ dàng lựa chọn sản phẩm phù hợp.
- **Tìm kiếm và lọc sản phẩm**: Khách hàng có thể tìm kiếm và lọc sản phẩm theo tên
- **Giỏ hàng và thanh toán**: Hệ thống hỗ trợ các cổng thanh toán, đảm bảo giao dịch an toàn và bảo mật.
- **Xem chương trình khuyến mãi**: Áp dụng mã giảm giá và các chương trình ưu đãi để tiết kiệm chi phí cho khách hàng.

### **Trang Quản Lý**

 -**Quản lý quầy**: Theo dõi, cập nhật thông tin quầy bán hàng, nhân viên phụ trách và tình trạng hoạt động.
- **Quản lý sản phẩm**: Cập nhật thông tin, giá cả, hình ảnh sản phẩm và kiểm soát kho hàng.
- **Quản lý khuyến mãi**: Phê duyệt, từ chối hoặc điều chỉnh chương trình khuyến mãi để tối ưu doanh số.
- **Quản lý mua lại**: Xử lý giao dịch mua lại trang sức từ khách hàng, kiểm tra chất lượng và định giá sản phẩm.
- **Quản lý nhân viên**: Quản lý hồ sơ nhân sự, phân quyền và theo dõi hiệu suất làm việc.
- **Quản lý doanh thu**: Tổng hợp các quá trình theo dõi, phân tích và tối ưu hóa nguồn thu từ hoạt động bán hàng, nhằm đảm bảo lợi nhuận và sự phát triển bền vững.
- **Khai báo**: Ghi nhận, báo cáo các thông tin quan trọng liên quan đến hoạt động kinh doanh.
- **Quản lý tích điểm**: Theo dõi chương trình tích điểm, cập nhật lịch sử giao dịch và các ưu đãi cho khách hàng.
- **Lịch sử mua hàng**: Phần dữ liệu ghi nhận tất cả các giao dịch mua sắm mà khách hàng đã thực hiện trên hệ thống.
- **Dashboard**: Cung cấp cái nhìn tổng quan về hoạt động kinh doanh thông qua dữ liệu trực quan và biểu đồ phân tích.

---

## **Yêu Cầu Hệ Thống**

- **Ngôn ngữ lập trình**: Python 3.x
- **Framework**: Django
- **Cơ sở dữ liệu**: SQLite hoặc PostgreSQL
- **Môi trường ảo hóa**: Sử dụng môi trường ảo (virtual environment) để quản lý thư viện phụ thuộc và tối ưu hóa quá trình phát triển.

---

## **Hướng Dẫn Triển Khai**

### **Bước 1**: Sao Chép Mã Nguồn
```bash
git clone https://github.com/your-repo/jewelry-store.git
cd jewelry-store
```

### **Bước 2**: Cấu Hình Môi Trường
```bash
python -m venv django_venv
source django_venv/bin/activate  # macOS/Linux
django_venv\Scripts\activate  # Windows
```

### **Bước 3**: Cài Đặt Thư Viện Phụ Thuộc
```bash
pip install -r requirements.txt
```

### **Bước 4**: Khởi Chạy Hệ Thống
```bash
python manage.py migrate
python manage.py runserver
```

---

## **Hướng Dẫn Sử Dụng**

- **Trang khách hàng**: Truy cập vào [http://127.0.0.1:8000/](http://127.0.0.1:8000/) để mua sản phẩm và thực hiện thanh toán.
- **Trang quản lý**: Truy cập vào [http://127.0.0.1:8001/](http://127.0.0.1:8001/) để quản lý đơn hàng, sản phẩm và chương trình khuyến mãi.
- **Trang admin**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) 
- **Khách hàng**: Có thể đăng ký tài khoản, đăng nhập và thực hiện các giao dịch mua sắm.
- **Nhân viên**: Có thể quản lý thông tin sản phẩm, đơn hàng, khách hàng và xem báo cáo.

---

## **Đóng Góp & Phát Triển**

Chúng tôi khuyến khích cộng đồng tham gia vào việc cải tiến hệ thống. Nếu bạn có ý tưởng hoặc cải tiến, hãy fork repository và gửi pull request để đóng góp vào dự án.

---

## **Liên Hệ & Hỗ Trợ (DEMO)**

- **Email**: info@jewelrystore.com
- **Website**: [https://jewelrystore.com](https://jewelrystore.com)
- **Hotline**: 0123-456-789

---
# Preview
## Trang 1
![image](https://github.com/user-attachments/assets/a3929e62-a23f-4b74-b93b-9a9318e0481b)
![image](https://github.com/user-attachments/assets/7d265c69-4f56-4a66-919b-0e94fbca1a9e)
![image](https://github.com/user-attachments/assets/dbcf500e-efb1-4089-a16a-3a2a61e0c473)
![image](https://github.com/user-attachments/assets/cd5b4303-f1c2-4174-b89c-cd736e0394ba)
![image](https://github.com/user-attachments/assets/4757d6dd-709b-46a4-8087-8e6b2bca6787)
![image](https://github.com/user-attachments/assets/fa52bfdf-e37f-4727-b707-349e8dd6f2ae)
![image](https://github.com/user-attachments/assets/a290e48c-e09b-467e-8284-26cdf3e6d143)
## Trang 2
![image](https://github.com/user-attachments/assets/ae943aeb-3d6d-4aa7-a8e9-a79e09e51ebb)
![image](https://github.com/user-attachments/assets/5eacade7-68f3-4cf1-a7d8-8921295e41ef)
![image](https://github.com/user-attachments/assets/fc9e4552-bf51-45ff-90a6-bcd46b203ec4)
![image](https://github.com/user-attachments/assets/f4a7709f-cc53-43f4-9c88-b173bbc6ef78)
![image](https://github.com/user-attachments/assets/31bcef77-7d8b-4f20-98d7-a85eacb6bc9e)
![image](https://github.com/user-attachments/assets/3e28899c-75c4-46a1-8a3b-6ffbac2f1f1b)



Chúng tôi mong muốn mang đến trải nghiệm mua sắm trang sức trực tuyến tuyệt vời nhất cho khách hàng!

---

### **PROJECT SOFTWARE TECHNOLOGY - GROUP 8 - JEWELRY SALE STORE**

---

