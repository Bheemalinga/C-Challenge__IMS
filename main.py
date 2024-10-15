import time
import sys
from dao.InsuranceServiceImpl import InsuranceServiceImpl
from entity.Policy import Policy
from exception.PolicyException import PolicyNotFoundException

class Policy_Management:
    def __init__(self):
        self.database_handshake = InsuranceServiceImpl()  # used to interact with the database

    def display_menu(self):
        while True:
            print("\n-----> Insurance Management System Menu <-----")
            self.typewriter("\t1. Create New Policy\n\t2. Retrieve Policy by ID\n\t3. View All Policies\n\t4. Modify Existing Policy\n\t5. Remove Policy\n\t6. Exit Application",speed = 0.01)
            print("<-------------------------------------------->\n")

            Options = input("\tSelect an option: ")

            if Options == '1':
                self.policy_creation()
            elif Options == '2':
                self.fetch_policy()
            elif Options == '3':
                self.view_all_policies()
            elif Options == '4':
                self.modify_policy()
            elif Options == '5':
                self.remove_policy()
            elif Options == '6':
                self.typewriter("\n\nThank you for using the Insurance Management System. Goodbye!\n\n",speed = 0.01)
                time.sleep(1)
                break
            else:
                print("Option doesn't exist, Please select a valid option.")
                time.sleep(2)

    def policy_creation(self):
        try:
            policy_identifier = int(input("Enter policy ID: "))
            policy_name = input("Enter policy name: ")
            policy_premium = float(input("Enter premium amount: "))
            policy_coverage = float(input("Enter coverage amount: "))

            new_policy = Policy(policy_identifier, policy_name, policy_premium, policy_coverage)
            result = self.database_handshake.createPolicy(new_policy)

            if result:
                time.sleep(1.5)
                print("\nPolicy created successfully.\n")
            else:
                print("Failed to create the policy.")
        except Exception as e:
            print(f"Error in policy creation: {e}")

    def fetch_policy(self):
        try:
            policy_identifier = int(input("Enter policy ID: "))
            retrieved_policy = self.database_handshake.getPolicy(policy_identifier)

            if retrieved_policy:
                print(retrieved_policy)
        except Exception as e:
            print(f"Error in policy retrieval: {e}")

    def view_all_policies(self):
        try:
            policies_list = self.database_handshake.getAllPolicies()

            if policies_list:
                print("\nAll Available Policies are as follows:")
                time.sleep(1)
                for i,policy in enumerate(policies_list):
                    print(i+1,". ",policy)
                    time.sleep(1)
            else:
                print("policies Unavailable.")
        except Exception as e:
            print(f"Error in retrieval of policies: {e}")

    def modify_policy(self):
        try:
            policy_identifier = int(input("Enter policy ID to update: "))
            existing_policy = self.database_handshake.getPolicy(policy_identifier)

            if existing_policy:
                print(f"Current details for Policy ID {policy_identifier}: {existing_policy}") # Displaying the current details of the policy

                updated_name = input(f"Enter new policy name (current: {existing_policy.get_plan_name()}): ") or existing_policy.get_plan_name()
                updated_premium = float(input(f"Enter new premium amount (current: {existing_policy.get_premium_cost()}): ") or existing_policy.get_premium_cost())
                updated_coverage = float(input(f"Enter new coverage amount (current: {existing_policy.get_coverage_limit()}): ") or existing_policy.get_coverage_limit())

                existing_policy.set_plan_name(updated_name)
                existing_policy.set_premium_cost(updated_premium)
                existing_policy.set_coverage_limit(updated_coverage)

                result = self.database_handshake.updatePolicy(existing_policy)
                if result:
                    print(f"Policy {policy_identifier} updation done successfully.")
                else:
                    print("Failed to update the policy.")
            else:
                print(f"Policy with ID {policy_identifier} unavailable.")
        except Exception as e:
            print(f"Error in modification of Policy: {e}")

    def remove_policy(self):
        try:
            policy_identifier = int(input("Enter policy ID that needs to be deleted: "))
            result = self.database_handshake.deletePolicy(policy_identifier)

            if result:
                print(f"Policy {policy_identifier} is cleared from the List")
            else:
                print(f"Failure in deletion of policy with ID {policy_identifier}.")
        except Exception as e:
            print(f"Error in policy deletion: {e}")


    def typewriter(self, text, speed):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()


def main():
    policy_manager = Policy_Management()
    policy_manager.display_menu()

if __name__ == "__main__":
    main()
