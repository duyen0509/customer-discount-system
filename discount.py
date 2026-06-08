def calculate_discount(tong_mua_hang):
    if tong_mua_hang >= 50000000:
        return 0.1
    return 0


if __name__ == "__main__":
    tong_mua_hang = float(input("Nhập tổng giá trị mua hàng trong năm: "))

    discount = calculate_discount(tong_mua_hang)

    if discount > 0:
        print("Khách hàng thân thiết.")
        print(f"Mức giảm giá: {discount * 100}%")
    else:
        print("Khách hàng không được giảm giá.")