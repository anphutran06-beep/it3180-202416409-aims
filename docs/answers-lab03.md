# Thảo luận Lab 03 - Bugfix flow, xung đột & hoàn tác

1. **Merge base là gì?**
   - Merge base là commit chung gần nhất giữa hai nhánh đang xét, dùng làm mốc để Git tính toán các thay đổi khác biệt khi merge hoặc rebase.
2. **Vì sao `master`/`release/*` phải dùng `revert` thay vì `reset`?**
   - Vì đây là các nhánh công khai và là baseline chính. `reset` làm thay đổi lịch sử trên remote gây hỏng việc của người khác, trong khi `revert` tạo commit đảo ngược an toàn mà không làm mất lịch sử cũ.
