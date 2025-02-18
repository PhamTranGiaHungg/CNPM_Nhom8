CREATE SCHEMA `quanlycuahangtrangsuc` ;

-- Bảng sản phẩm (products)
CREATE TABLE products (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    name VARCHAR(255) NOT NULL, -- Tên sản phẩm
    barcode VARCHAR(50) UNIQUE NOT NULL, -- Mã vạch
    category VARCHAR(100) NOT NULL, -- Loại sản phẩm
    gold_price DECIMAL(10, 2) NOT NULL, -- Giá vàng
    labor_cost DECIMAL(10, 2) NOT NULL, -- Công gia công
    crafting_cost DECIMAL(10, 2) NOT NULL, -- Chi phí gia công
    stock INT NOT NULL, -- Số lượng tồn kho
    description TEXT, -- Mô tả sản phẩm
    supplier_id INT -- Khóa ngoại liên kết với bảng nhà cung cấp (nếu có)
);

-- Bảng khách hàng (customers)
CREATE TABLE customers (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    name VARCHAR(255) NOT NULL, -- Tên khách hàng
    phone VARCHAR(15) UNIQUE NOT NULL, -- Số điện thoại
    email VARCHAR(255), -- Email khách hàng
    address TEXT, -- Địa chỉ khách hàng
    loyalty_points INT DEFAULT 0, -- Điểm tích lũy
    transaction_history JSON -- Lịch sử giao dịch (dạng JSON lưu hóa đơn và thông tin liên quan)
);

-- Bảng hóa đơn (invoices)
CREATE TABLE invoices (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    customer_id INT, -- Khóa ngoại liên kết với bảng customers
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Ngày giao dịch
    total_amount DECIMAL(10, 2) NOT NULL, -- Tổng tiền hóa đơn
    discount DECIMAL(5, 2) DEFAULT 0, -- Chiết khấu (nếu có)
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL
);

-- Bảng phụ: Chi tiết sản phẩm trong hóa đơn (invoice_products)
-- Để dễ dàng truy vấn các sản phẩm thuộc hóa đơn
CREATE TABLE invoice_products (
    invoice_id INT, -- Khóa ngoại liên kết với bảng invoices
    product_id INT, -- Khóa ngoại liên kết với bảng products
    quantity INT NOT NULL, -- Số lượng sản phẩm
    price DECIMAL(10, 2) NOT NULL, -- Giá bán
    FOREIGN KEY (invoice_id) REFERENCES invoices(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Bảng khuyến mãi (promotions)
CREATE TABLE promotions (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    name VARCHAR(255) NOT NULL, -- Tên chương trình khuyến mãi
    description TEXT, -- Mô tả khuyến mãi
    discount_rate DECIMAL(5, 2) NOT NULL, -- Mức chiết khấu (phần trăm)
    start_date TIMESTAMP NOT NULL, -- Ngày bắt đầu
    end_date TIMESTAMP NOT NULL -- Ngày kết thúc
);

-- Bảng chi tiết khuyến mãi theo sản phẩm (promotion_products)
CREATE TABLE promotion_products (
    promotion_id INT, -- Khóa ngoại liên kết với bảng promotions
    product_id INT, -- Khóa ngoại liên kết với bảng products
    FOREIGN KEY (promotion_id) REFERENCES promotions(id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Bảng mua lại hàng (buybacks)
CREATE TABLE buybacks (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    product_id INT, -- Khóa ngoại liên kết với bảng products
    buyback_rate DECIMAL(5, 2) NOT NULL, -- Tỷ lệ mua lại (% giá bán)
    fixed_rate DECIMAL(10, 2), -- Giá cố định (nếu có)
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Bảng lịch sử mua lại (buyback_history)
CREATE TABLE buyback_history (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    customer_id INT, -- Khóa ngoại liên kết với bảng customers
    product_id INT, -- Khóa ngoại liên kết với bảng products
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Ngày giao dịch mua lại
    amount DECIMAL(10, 2) NOT NULL, -- Số tiền đã mua lại
    FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE SET NULL,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE SET NULL
);

-- Bảng nhà cung cấp (suppliers)
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY, -- Khóa chính, tự động tăng
    name VARCHAR(255) NOT NULL, -- Tên nhà cung cấp
    phone VARCHAR(15) NOT NULL, -- Số điện thoại
    email VARCHAR(255), -- Email liên hệ
    address TEXT -- Địa chỉ nhà cung cấp
);

