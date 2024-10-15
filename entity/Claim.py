class Claim:
    def __init__(self, claim_id=None, claim_num=None, file_date=None, amount=None, claim_status=None, policy_id=None, customer_id=None):
        # Private attributes for claim details
        self.__claim_id = claim_id
        self.__claim_num = claim_num
        self.__file_date = file_date
        self.__amount = amount
        self.__claim_status = claim_status
        self.__policy_id = policy_id
        self.__customer_id = customer_id

    # Getter methods to access private attributes
    def get_claim_id(self):
        return self.__claim_id

    def get_claim_num(self):
        return self.__claim_num
    
    def get_file_date(self):
        return self.__file_date
    
    def get_amount(self):
        return self.__amount
    
    def get_claim_status(self):
        return self.__claim_status
    
    def get_policy_id(self):
        return self.__policy_id
    
    def get_customer_id(self):
        return self.__customer_id
    
    # Setter methods to modify private attributes
    def set_claim_id(self, claim_id):
        self.__claim_id = claim_id

    def set_claim_num(self, claim_num):
        self.__claim_num = claim_num

    def set_file_date(self, file_date):
        self.__file_date = file_date

    def set_amount(self, amount):
        self.__amount = amount

    def set_claim_status(self, claim_status):
        self.__claim_status = claim_status

    def set_policy_id(self, policy_id):
        self.__policy_id = policy_id

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    # String representation of the InsuranceClaim object
    def __str__(self):
        return (f"InsuranceClaim(claim_id = {self.__claim_id}, claim_num = {self.__claim_num}, file_date = {self.__file_date}, amount = {self.__amount}, claim_status = {self.__claim_status}, policy_id = {self.__policy_id}, customer_id = {self.__customer_id})")