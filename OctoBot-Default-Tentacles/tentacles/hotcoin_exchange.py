from trading_backend.exchanges import Exchange  # Assuming base class

class HotcoinExchange(Exchange):
    @staticmethod
    def get_name() -> str:
        return "hotcoin"

    @staticmethod
    def is_sponsoring() -> bool:
        return False  # Or True if sponsored
