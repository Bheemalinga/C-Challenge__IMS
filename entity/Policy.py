class Policy:
    def __init__(self, policy_id=None, plan_name=None, premium_cost=None, coverage_limit=None):
        # Private attributes for policy details
        self.__policy_id = policy_id
        self.__plan_name = plan_name
        self.__premium_cost = premium_cost
        self.__coverage_limit = coverage_limit

    # Getter methods to access private attributes
    def get_policy_id(self):
        return self.__policy_id
    
    def get_plan_name(self):
        return self.__plan_name
    
    def get_premium_cost(self):
        return self.__premium_cost
    
    def get_coverage_limit(self):
        return self.__coverage_limit

    # Setter methods to modify private attributes
    def set_policy_id(self, policy_id):
        self.__policy_id = policy_id

    def set_plan_name(self, plan_name):
        self.__plan_name = plan_name

    def set_premium_cost(self, premium_cost):
        self.__premium_cost = premium_cost

    def set_coverage_limit(self, coverage_limit):
        self.__coverage_limit = coverage_limit

    def __str__(self):
        return "Policy_id = " + str(self.__policy_id) + " || plan_name = " + str(self.__plan_name) + " || premium_cost = " + str(self.__premium_cost) + " || coverage_limit = " + str(self.__coverage_limit)
