# Hệ thống Quản lý Bán hàng và Đặt hàng Trực tuyến SOA

Bộ khung khởi tạo theo SRS, báo cáo và bảng task của nhóm: NGINX Gateway, 5 dịch vụ FastAPI và 5 schema MySQL độc lập theo Database-per-Service. Các API hiện có health check; nghiệp vụ sẽ được bổ sung theo danh sách task.

## Công nghệ
Python 3.11+, FastAPI, Uvicorn, MySQL 8.0, NGINX, HTML/CSS/JavaScript.

## Chạy bằng Docker Compose
Cần Docker Desktop đang chạy. Tại thư mục gốc:

```powershell
docker compose up --build
```

Mở http://localhost:8080. OpenAPI: http://localhost:8001/docs đến http://localhost:8005/docs. Dừng bằng Ctrl+C; chạy nền với `docker compose up --build -d`.

## Thư mục
- `services/{auth,product,inventory,order,payment}`: ứng dụng FastAPI độc lập.
- `gateway/nginx.conf`: định tuyến API và phục vụ web tĩnh.
- `database/init.sql`: tạo 5 schema.
- `frontend/`: trang chủ khởi tạo.

## Trạng thái khung
- Chưa có bảng nghiệp vụ hoặc ORM model.
- Mỗi service chỉ cung cấp `GET /health`; đăng nhập, sản phẩm, đặt hàng, kho và thanh toán chưa triển khai.
- Các route NGINX là tiền tố dự kiến theo tài liệu.
- MySQL đang dùng mật khẩu local mặc định `root`; đổi trước khi triển khai dùng chung.
