class Client:
    def __init__(self, customer_id=None, customer_name=None, contact_details=None, policy_ref=None):
        # Private attributes for client details
        self.__customer_id = customer_id
        self.__customer_name = customer_name
        self.__contact_details = contact_details
        self.__policy_ref = policy_ref

    # Getter methods to access private attributes
    def get_customer_id(self):
        return self.__customer_id

    def get_customer_name(self):
        return self.__customer_name
    
    def get_contact_details(self):
        return self.__contact_details
    
    def get_policy_ref(self):
        return self.__policy_ref   
    
    # Setter methods to modify private attributes
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_contact_details(self, contact_details):
        self.__contact_details = contact_details

    def set_policy_ref(self, policy_ref):
        self.__policy_ref = policy_ref

    # String representation of the Client object
    def __str__(self):
        return (f"Client(customer_id = {self.__customer_id}, customer_name = {self.__customer_name}, contact_details = {self.__contact_details}, policy_ref = {self.__policy_ref})")