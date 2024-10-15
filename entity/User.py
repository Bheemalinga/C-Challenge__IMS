class User:
    def __init__(self, user_id=None, user_name=None, user_password=None, user_role=None):
        # Private attributes for user details
        self.__user_id = user_id
        self.__user_name = user_name
        self.__user_password = user_password
        self.__user_role = user_role

    # Getter methods to access private attributes
    def get_user_id(self):
        return self.__user_id
    
    def get_user_name(self):
        return self.__user_name
    
    def get_user_password(self):
        return self.__user_password
    
    def get_user_role(self):
        return self.__user_role
    
    # Setter methods to modify private attributes
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_user_name(self, user_name):
        self.__user_name = user_name

    def set_user_password(self, user_password):
        self.__user_password = user_password

    def set_user_role(self, user_role):
        self.__user_role = user_role

    # String representation of the User object
    def __str__(self):
        return (f"User(user_id = {self.__user_id}, user_name = {self.__user_name}, password = ******, user_role = {self.__user_role})")