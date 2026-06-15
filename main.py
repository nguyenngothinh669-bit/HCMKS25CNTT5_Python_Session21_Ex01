import logging
import re
from exceptions import InvalidAmountError, InsufficientBalanceError
from momo_wallet import deposit, transfer


def display_menu() -> None:
    """Hiển thị giao diện menu chức năng."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("===============================================")


def get_valid_amount(prompt: str) -> int:
    """Yêu cầu nhập số tiền và bắt lỗi ValueError nếu nhập chữ thay vì số."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            logging.error("ValueError: Invalid numeric input for deposit.")
            print("Lỗi: Vui lòng nhập số tiền hợp lệ.")


def get_valid_phone(prompt: str) -> str:
    """Yêu cầu nhập và kiểm tra định dạng số điện thoại (phải đủ 10 số)."""
    while True:
        phone = input(prompt).strip()
        if re.match(r"^\d{10}$", phone):
            return phone
        print("Lỗi: Số điện thoại không hợp lệ (Phải bao gồm 10 chữ số).")


def main() -> None:
    """Hàm khởi chạy hệ thống, điều phối luồng dữ liệu."""
    balance = 0 

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            print("\n--- NẠP TIỀN VÀO VÍ ---")
            amount = get_valid_amount("Nhập số tiền cần nạp: ")
            try:
                balance = deposit(balance, amount)
                print(f"\nNạp tiền thành công: +{amount:,} VND")
                print(f"Số dư hiện tại: {balance:,} VND")
            except InvalidAmountError as e:
                print(f"Lỗi: {e}")

        elif choice == "2":
            print("\n--- CHUYỂN TIỀN ---")
            phone = get_valid_phone("Nhập số điện thoại người nhận: ")
            amount = get_valid_amount("Nhập số tiền cần chuyển: ")
            try:
                balance = transfer(balance, amount, phone)
                print(f"\nChuyển tiền thành công tới số điện thoại {phone}.")
                print(f"Số tiền đã chuyển: {amount:,} VND")
                print(f"Số dư còn lại: {balance:,} VND")
            except (InvalidAmountError, InsufficientBalanceError) as e:
                print(f"{e}")
                if isinstance(e, InsufficientBalanceError):
                    print(f"Số dư hiện tại: {balance:,} VND")

        elif choice == "3":
            print("\n--- SỐ DƯ VÍ MOMO ---")
            print(f"Số dư hiện tại: {balance:,} VND")
            logging.info(f"Balance checked. Current Balance: {balance}")

        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng dịch vụ")
            logging.info("System shutdown")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại từ 1 đến 4.")


if __name__ == "__main__":
    main()