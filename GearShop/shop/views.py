from django.shortcuts import render

# View trang chủ
def home(request):
    return render(request, 'shop/home.html')

# View chi tiết sản phẩm
def product_detail(request, id):
    # Giả lập dữ liệu sản phẩm
    product = {
        'id': id,
        'name': 'Laptop XYZ',
        'price': 1200,
        'description': 'Mô tả ngắn gọn về sản phẩm Laptop XYZ.'
    }
    return render(request, 'shop/product_detail.html', {'product': product})