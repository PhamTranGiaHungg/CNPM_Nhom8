{% load static %}

<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8"> <!-- Đặt mã hóa ký tự -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- Cấu hình để chạy trên các trình duyệt hiện đại -->
        <meta name="viewport" content="width=device-width, initial-scale=1"> <!-- Đảm bảo trang web hiển thị tốt trên mọi thiết bị -->
        <meta name="description" content=""> <!-- Mô tả trang web -->
        <title>Cửa Hàng Trang Sức</title> <!-- Tiêu đề của trang web -->

        <!-- CSS -->
        <!-- Kết nối với CSS của Bootstrap từ CDN -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <!-- Liên kết đến các tệp CSS tùy chỉnh cho giao diện -->
        <link href="{% static 'app/css/style.css' %}" rel="stylesheet">
        <link href="{% static 'app/css/owl.carousel.min.css' %}" rel="stylesheet">
        <link href="{% static 'app/css/all.min.css' %}" rel="stylesheet">
        <!-- Kết nối thêm CSS của Bootstrap phiên bản cũ -->
        <!-- <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous"> -->
        <!-- CSS chính của trang -->
        <link rel="stylesheet" type="text/css" href="{% static 'app/css/main.css' %}">
        <!-- Favicon của trang web -->
        <link rel="icon" href="{% static 'app/images/favicon.ico' %}" type="image/x-icon">

        <!-- JS -->
        <!-- Kết nối với các thư viện JS cần thiết -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js" integrity="sha512-v2CJ7UaYy4JwqLDIrZUI/4hqeoQieOmAZNXBeQyjo21dadnwR+8ZaIJVT8EE2iyI61OV8e6M8PP2/4hpQINQ/g==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
        <!-- Kết nối các tệp JS tùy chỉnh -->
        <script src="{% static 'app/js/s3.js' %}"></script>
        <script src="{% static 'app/js/all.min.js' %}"></script>
        <script src="{% static 'app/js/myscript.js' %}"></script>

        <script type="text/javascript">
            // Lấy thông tin người dùng từ server và gán vào biến user
            var user = '{{ request.user }}';

            // Hàm lấy giá trị cookie theo tên
            function getCookie(name) {
                let cookieValue = null;
                if (document.cookie && document.cookie !== '') {
                    const cookies = document.cookie.split(';');
                    for (let i = 0; i < cookies.length; i++) {
                        const cookie = cookies[i].trim();
                        if (cookie.substring(0, name.length + 1) === (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }

            // Lấy giá trị CSRF token từ cookie để bảo mật yêu cầu
            const csrftoken = getCookie('csrftoken');
        </script>

        <style>
            /* Các kiểu dáng cho các phần tử trong navbar */
            .navbar .nav-link {
                font-size: 20px;
            }

            .navbar .navbar-brand {
                font-size: 25px;
            }

            .navbar .dropdown-menu .dropdown-item {
                font-size: 21px;
            }

            .form-control {
                font-size: 21px;
            }

            .btn-outline-success {
                font-size: 21px;
            }
        </style>
    </head>

    <body>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                
                    <!-- Logo trang web -->
                <a class="navbar-brand" href="{% url 'home' %}">
                    <img src="{% static 'app/images/jewelrylogo.png' %}" id="logo" width="120" height="100" alt="Logo">
                </a>
                <!-- Nút điều hướng trên di động -->
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <!-- Danh sách các mục trên navbar -->
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav  me-auto mb-2 mb-lg-0">
                        <!-- Mục Trang chủ -->
                        <li class="nav-item">
                            <a class="nav-link active" href="{% url 'home' %}">Trang chủ</a>
                        </li>
                        
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Danh mục sản phẩm</a>
                            <ul class="dropdown-menu">
                                {% for category in categories %} 
                                <li><a class="dropdown-item" href="{% url 'category' %}?category={{ category.slug }}">{{ category.name }}</a></li>
                                {% endfor %}
                            </ul>
                        </li>
                        <!-- Mục giỏ hàng -->
                        <li class="nav-item">
                            <a class="nav-link active" href="{% url 'cart' %}">Giỏ hàng</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link active" href="{% url 'contact' %}">Liên hệ</a>
                        </li>
                    </ul>
                    <div class="navbar-right"> <!-- Thêm thẻ div này để căn chỉnh-->
                        <!-- Form tìm kiếm -->
                        <form class="d-flex" role="search" method = POST action = "{% url 'search' %}">
                            {% csrf_token %}
                            <input class="form-control me-2" type="search" placeholder="Nhập" aria-label="Search" name = "searched">
                            <button class="btn btn-outline-success" type="submit">Tìm kiếm</button>
                        </form>


                        <!-- Mục Người dùng -->
                         <div class="form-inline my-2 my-lg-0 {% if not user.is_authenticated %}d-none{% endif %}">
                            <span> Xin chào! {{ request.user }}</span>
                             <span><a href="{% url 'logout' %}">  Đăng xuất</a></span>
                         </div>
                    
                    
                    
                         <div class="form-inline my-2 my-lg-0 {% if user.is_authenticated %}d-none{% endif %}">
                              <a class="nav-link" href="{% url 'login' %}">Đăng nhập</a>
                              <a class="nav-link" href="{% url 'register' %}">Đăng ký</a>
                          </div>


                        <!-- Mục Logo Giỏ hàng -->
                         <div class="form-inline my-2 my-lg-0 d-flex align-items-center">
                                <a href="{% url 'cart' %}" class="cart-link">
                                   <img id="cart-icon" class="img-fluid" style="width: 50px;" src="{% static 'images/shoppingcart.png' %}" alt="Cart Icon">
                                </a>
                                <p id="cart-total" class="fs-8 ms-0">{{ cartItems }}</p>
                         </div>
                       </div>
                    
                </div>
            </div>
        </nav>

        <!-- Các block nội dung trang web -->
        {% block banner_slider %}{% endblock banner_slider %}
        {% block main-content %}{% endblock main-content %}
        <!--giao diện cart-->
        {% block cart_content %}{% endblock cart_content %}
        {% block content_checkout %}{% endblock content_checkout %}
        {% block register %}{% endblock register %}
    

        <!-- Footer -->
        <footer class="container-fluid bg-success text-center fixed-bottom p-2 mt-5">
            Phiên bản bản quyền 2024
        </footer>

        <!-- Kết nối JavaScript cho giỏ hàng -->
        <script src="{% static 'app/js/cart.js' %}"></script>
    </body>
</html>
