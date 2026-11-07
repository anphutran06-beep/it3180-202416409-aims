# Thảo luận Lab 04 - Release flow & Phiên bản phát hành

1. **Vì sao release/* không merge vào master?**
   - Nhánh `release/*` dùng để đóng băng phiên bản đã phát hành. Việc không merge ngược giúp tránh ghi đè mã nguồn mới trên `master`. Bản vá lỗi sẽ đi qua hotfix và lan truyền bằng `cherry-pick`.
2. **So sánh Release Flow (của học phần) với GitFlow?**
   - **Release Flow:** Đơn giản hóa, dùng `master` làm nhánh phát triển chính, rẽ nhánh `release/labXX` nộp bài và `hotfix/*` vá lỗi mà không cần nhánh `develop`.
   - **GitFlow:** Phức tạp hơn với hai nhánh dài hạn `main` và `develop`, kết hợp nhiều nhánh phụ trợ cho dự án lớn.
3. **Vì sao lên 1.0.0 mà không phải 0.4.0?**
   - Theo SemVer, mốc `1.0.0` đánh dấu phiên bản ổn định chính thức đầu tiên, hoàn thiện tính năng cốt lõi sẵn sàng bàn giao cho người dùng sau giai đoạn thử nghiệm `0.y.z`.
