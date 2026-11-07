# Thảo luận Lab 01 - Thiết lập môi trường & Refactor flow

1. **Vì sao dùng `git mv`?**
   - `git mv` thực hiện đồng thời hai việc: đổi tên/di chuyển tệp và đưa thẳng vào staging area. Thao tác này giúp Git nhận diện đây là hành động đổi tên thay vì xóa tệp cũ tạo tệp mới, giữ nguyên lịch sử commit để tra cứu bằng `git log --follow`.
2. **`release/lab01` có phải baseline không?**
   - Có. `release/lab01` là baseline đánh dấu trạng thái ổn định, được đóng băng tại thời điểm nộp bài để định danh và kiểm toán.
3. **Vì sao không commit thẳng `master` dù làm một mình?**
   - Để hình thành thói quen tuân thủ Release Flow chuyên nghiệp, mô phỏng đúng môi trường doanh nghiệp thực tế, kiểm soát thay đổi chặt chẽ qua Pull Request.
