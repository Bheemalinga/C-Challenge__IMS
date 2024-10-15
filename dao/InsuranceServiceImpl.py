from dao.IPolicyService import IPolicyService
from entity.Policy import Policy
from util.DBConnection import DBConnection
from exception.PolicyException import PolicyNotFoundException

class InsuranceServiceImpl(IPolicyService):
    def __init__(self):
        self.connection = DBConnection.getConnection()
        if self.connection is None:
            raise Exception("Database connection Unsuccesful")
            
    def createPolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()
            query = """INSERT INTO Policy (policy_id, policy_name, premium_cost, coverage_limit)
                       VALUES (?, ?, ?, ?)"""
            cursor.execute(query, (policy.get_policy_id(), policy.get_plan_name(),
                                   policy.get_premium_cost(), policy.get_coverage_limit()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error while creating policy: {e}")
            return False

    def getPolicy(self, policy_id: int):
        try:
            cursor = self.connection.cursor()
            query = """SELECT * FROM Policy WHERE policy_id = ?"""
            cursor.execute(query, (policy_id,))
            row = cursor.fetchone()

            if row:
                policy = Policy(row[0], row[1], row[2], row[3])
                return policy
            else:
                raise PolicyNotFoundException(f"Policy with ID {policy_id} not found.")
        except PolicyNotFoundException as e:
            print(e)
            return None
        except Exception as e:
            print(f"Error while fetching policy: {e}")
            return None

    def getAllPolicies(self):
        try:
            cursor = self.connection.cursor()
            query = """SELECT * FROM Policy"""
            cursor.execute(query)
            rows = cursor.fetchall()

            policies = []
            for row in rows:
                policy = Policy(row[0], row[1], row[2], row[3])
                policies.append(policy)
            return policies

        except Exception as e:
            print(f"Error in fetching the policies: {e}")
            return []

    def updatePolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()
            query = """UPDATE Policy
                       SET policy_name = ?, premium_cost = ?, coverage_limit = ?
                       where policy_id = ?"""
            cursor.execute(query, (policy.get_plan_name(), policy.get_premium_cost(),
                                   policy.get_coverage_limit(), policy.get_policy_id()))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error in updating policy: {e}")
            return False

    def deletePolicy(self, policy_id: int):
        try:
            cursor = self.connection.cursor()
            query = """SELECT * FROM Policy WHERE policy_id = ?"""
            cursor.execute(query, (policy_id,))
            row = cursor.fetchone()
            if not row:
                raise PolicyNotFoundException(f"Policy with ID {policy_id} not found.")
                
            query = """DELETE FROM Policy where policy_id = ?"""
            cursor.execute(query, (policy_id,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error in deleting policy: {e}")
            return False