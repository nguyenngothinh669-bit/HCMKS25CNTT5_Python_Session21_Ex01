import logging
from exceptions import InvalidAmountError, InsufficientBalanceError

logging.basicConfig(
    filename="momo_transactions.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def deposit(current_balance: int, amount: int) -> int:
    """Xử lý nghiệp vụ nạp tiền và trả về số dư mới.

    Raises:
        InvalidAmountError: Nếu số tiền nạp vào không hợp lệ (<= 0).
    """
    if amount <= 0:
        logging.error(
            f"InvalidAmountError: Attempted to process {amount} VND."
        )
        raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")

    new_balance = current_balance + amount
    logging.info(
        f"Deposit successful: +{amount} VND. "
        f"Current Balance: {new_balance}"
    )
    return new_balance


def transfer(current_balance: int, amount: int, phone: str) -> int:
    """Xử lý nghiệp vụ chuyển tiền và trả về số dư mới.

    Raises:
        InvalidAmountError: Nếu số tiền chuyển không hợp lệ (<= 0).
        InsufficientBalanceError: Nếu số dư hiện tại không đủ.
    """
    if amount <= 0:
        logging.error(
            f"InvalidAmountError: Attempted to process {amount} VND."
        )
        raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")

    if amount > current_balance:
        logging.error(
            f"InsufficientBalanceError: Attempted to transfer {amount} VND "
            f"with balance {current_balance} VND."
        )
        raise InsufficientBalanceError(
            "Giao dịch thất bại: Số dư của bạn không đủ."
        )

    # Cảnh báo giao dịch giá trị cao (>= 10,000,000 VND)
    if amount >= 10000000:
        logging.warning(
            f"High value transaction detected: {amount} VND to {phone}"
        )

    new_balance = current_balance - amount
    logging.info(
        f"Transfer successful: -{amount} VND to {phone}. "
        f"Current Balance: {new_balance}"
    )
    return new_balance