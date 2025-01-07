
// Lấy tất cả các nút "update-cart" trên trang
var updateBtns = document.getElementsByClassName('update-cart')

// Duyệt qua tất cả các nút và thêm sự kiện click
for (i=0;i < updateBtns.length;i++){
    updateBtns[i].addEventListener('click',function(){
        // Lấy productId và action từ dữ liệu trong nút
        var productId = this.dataset.product
        var action = this.dataset.action

        // In ra thông tin về productId và action
        console.log('productId',productId,'action',action)

        // In ra thông tin về người dùng
        console.log('user: ', user)

        // Kiểm tra xem người dùng đã đăng nhập chưa
        if (user === "AnonymousUser"){
            console.log('user not logged in') // Người dùng chưa đăng nhập
        } else {
            // Nếu người dùng đã đăng nhập, gọi hàm updateUserOrder
            updateUserOrder(productId,action)
        }
    })
}

// Hàm để cập nhật đơn hàng của người dùng
function updateUserOrder(productId,action){ 
    console.log('user logged in, success add') // Người dùng đã đăng nhập

    // Địa chỉ URL của API để cập nhật sản phẩm
    var url = '/update_item/'

    // Thực hiện một yêu cầu fetch đến API với phương thức POST
    fetch('/update_item/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',  // Loại dữ liệu là JSON
            'X-CSRFToken': csrftoken // Thêm CSRF token vào header để bảo vệ khỏi tấn công CSRF
        },
        body: JSON.stringify({'productId': productId, 'action': action}), // Dữ liệu gửi đi dưới dạng JSON
    })
    .then((response) => {
    return response.json()}) // Khi nhận được phản hồi từ server, chuyển thành JSON
    .then((data) =>{console.log(data) // In ra kết quả trả về từ server
    location.reload()
    })
}
