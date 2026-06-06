import functools

product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def display_products():
    print("\n--- DANH SÁCH TEM NHÃN ---")
    template = "Mã: {id:<10} | Tên: {name:<18} | Giá: {price:,} VND | Rating: {rating}*"
    for item in product_list:
        try:
            parts = item.split('-')
            data = {
                "id": parts[0],
                "name": parts[1],
                "price": int(parts[2]),
                "rating": float(parts[3])
            }
            print(template.format_map(data))
        except (IndexError, ValueError):
            print(f"Bỏ qua sản phẩm [{item.split('-')[0]}] do sai cấu trúc dữ liệu.")

def sort_products():
    product_list.sort(key=lambda x: (-float(x.split('-')[3]), int(x.split('-')[2])))
    print(">> Đã sắp xếp thành công! Cập nhật danh sách:")
    for i, item in enumerate(product_list, 1):
        p = item.split('-')
        print(f"{i}. {p[0]}-{p[1]}-{p[2]}-{p[3]}")

def calculate_total_value():
    prices = []
    for item in product_list:
        try:
            prices.append(int(item.split('-')[2]))
        except (IndexError, ValueError):
            continue
            
    total = functools.reduce(lambda a, b: a + b, prices)
    print(f"\nTổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

while True:
    choice = input("""
============== E-COMMERCE ANALYTICS ==============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng (reduce)
4. Đóng hệ thống
==================================================
Chọn chức năng (1-4): """)

    match choice:
        case "1":
            display_products()
        case "2":
            sort_products()
        case "3":
            calculate_total_value()
        case "4":
            print("Cảm ơn đã sử dụng hệ thống!")
            break
        case _:
            print("Lựa chọn không hợp lệ!")