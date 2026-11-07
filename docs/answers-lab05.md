# Thảo luận Lab 05 - Hotfix flow & Bảo trì nhiều phiên bản

1. **Ưu, nhược điểm của upstream first so với release first?**
   - **Upstream first (Sửa master trước, cherry-pick xuống release):** Ngăn triệt để lỗi ở tương lai, nhưng tốn công đồng bộ nếu cấu trúc mã nguồn đã thay đổi.
   - **Release first (Sửa trực tiếp trên release/hotfix rồi lan truyền lên master):** Xử lý sự cố nhanh chóng trên môi trường hiện tại, nhưng dễ bị sót nếu quên cherry-pick sang các nhánh khác.
2. **Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?**
   - Lệnh `git cherry -v origin/master origin/release/lab05` sẽ phát hiện các commit chưa được đưa sang nhánh tương ứng để cảnh báo thiếu sót.
