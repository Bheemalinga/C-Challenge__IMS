class Payment:
    def __init__(self, transaction_id=None, transaction_date=None, transaction_amount=None, customer_id=None):
        # Private attributes for payment details
        self.__transaction_id = transaction_id
        self.__transaction_date = transaction_date
        self.__transaction_amount = transaction_amount
        self.__customer_id = customer_id

    # Getter methods to retrieve private attributes
    def get_transaction_id(self):
        return self.__transaction_id

    def get_transaction_date(self):
        return self.__transaction_date
    
    def get_transaction_amount(self):
        return self.__transaction_amount
    
    def get_customer_id(self):
        return self.__customer_id
    
    # Setter methods to modify private attributes
    def set_transaction_id(self, transaction_id):
        self.__transaction_id = transaction_id

    def set_transaction_date(self, transaction_date):
        self.__transaction_date = transaction_date
    
    def set_transaction_amount(self, transaction_amount):
        self.__transaction_amount = transaction_amount

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # String representation of the Payment object
    def __str__(self):
        return (f"Payment(transaction_id = {self.__transaction_id}, transaction_date = {self.__transaction_date}, transaction_amount = {self.__transaction_amount}, customer_id = {self.__customer_id})")