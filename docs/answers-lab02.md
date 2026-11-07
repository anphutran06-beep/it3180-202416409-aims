# Thảo luận Lab 02 - Feature/Topic flow & Pull Request

1. **Vì sao phải đồng bộ master trước khi PR?**
   - Để kiểm tra xung đột (conflict) sớm và đảm bảo mã nguồn tích hợp chạy ổn định trên nền code mới nhất trước khi gửi reviewer phê duyệt.
2. **Khi nào không được rebase?**
   - Không bao giờ được rebase trên các nhánh đã chia sẻ công khai (`master`, `release/*`, hoặc nhánh chung của team) vì nó viết lại lịch sử commit, gây lệch pha và xung đột nặng cho người khác.
3. **`feature/*` khác `topic/*` ra sao?**
   - `feature/*` dùng cho tính năng cốt lõi của sản phẩm; `topic/*` dùng cho công việc phụ trợ, cấu hình, tài liệu hoặc thử nghiệm.
