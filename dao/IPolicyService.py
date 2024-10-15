from abc import ABC, abstractmethod
from entity.Policy import Policy

class IPolicyService(ABC):
    
    @abstractmethod
    def createPolicy(self, policy):
        # Create a new policy
        pass
    
    @abstractmethod
    def getPolicy(self, policy_id):
        # Retrieve a specific policy by its ID
        pass

    @abstractmethod
    def getAllPolicies(self):
        # Get a list of all policies
        pass

    @abstractmethod
    def updatePolicy(self, policy):
        # Update an existing policy
        pass

    @abstractmethod
    def deletePolicy(self, policy_id):
        # Delete a policy by its ID
        pass