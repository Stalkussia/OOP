from datetime import datetime
class Amount:
    def __init__(self, amount,transaction_type):
        self.amount = float(amount)
        self.transaction_type = str(transaction_type)
        self.timestamp = datetime.now()

    def __str__(self):
        return f"Amount: {self.amount}, Timestamp: {self.timestamp}, Transaction type: {self.transaction_type}"
