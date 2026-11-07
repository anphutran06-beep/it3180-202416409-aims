def search_by_category(items, category):
    """Tìm kiếm đĩa theo danh mục"""
    return [dvd for dvd in items if dvd.category.lower() == category.lower()]