"""Module định nghĩa các ngoại lệ tùy chỉnh cho hệ thống Ví MoMo."""


class InvalidAmountError(Exception):
    """Ngoại lệ xảy ra khi số tiền giao dịch nhỏ hơn hoặc bằng 0."""

    pass


class InsufficientBalanceError(Exception):
    """Ngoại lệ xảy ra khi số dư tài khoản không đủ để thực hiện giao dịch."""

    pass 

