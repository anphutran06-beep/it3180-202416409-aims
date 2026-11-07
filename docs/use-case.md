# Use Case Diagram & Description - AIMS Mini

## 1. Tóm tắt hệ thống
AIMS-mini là ứng dụng quản lý cửa hàng kinh doanh đĩa DVD, hỗ trợ các chức năng chính như:
- Quản lý giỏ hàng (thêm/xóa đĩa, tính tổng tiền, in giỏ hàng).
- Tìm kiếm đĩa theo tiêu đề hoặc danh mục.
- Xử lý các quy tắc ràng buộc số lượng đĩa tối đa trong giỏ hàng.

## 2. Các tác nhân (Actors)
- **Khách hàng / Người quản lý:** Tương tác trực tiếp với ứng dụng dòng lệnh (CLI) để thực hiện các thao tác mua hàng và quản lý giỏ hàng.

## 3. Các Use Case chính
- **UC01: Thêm đĩa vào giỏ hàng** (Kiểm tra giới hạn tối đa `MAX_NUMBERS_ORDERED = 20`).
- **UC02: Xóa đĩa khỏi giỏ hàng**.
- **UC03: Xem chi tiết và tính tổng tiền giỏ hàng**.
- **UC04: Tìm kiếm sản phẩm** (theo tên, danh mục, không phân biệt chữ hoa/thường ở bản vá hotfix).
