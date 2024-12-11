import random
import string

def generate_ec2_names():
    # List of authorized departments
    authorized_departments = ['marketing', 'accounting', 'finops']

    # Get user input for department
    department = input("Enter your department (Marketing, Accounting, FinOps): ").strip().lower()

    # Check if department is authorized
    if department not in authorized_departments:
        print("You are not authorized to use this Name Generator.")
        return

    # Get user input for number of EC2 instances
    num_instances = int(input("How many EC2 instances do you need names for? "))

    # Generate unique names for EC2 instances
    for i in range(num_instances):
        # Generate random characters and numbers
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))

        # Create unique name
        ec2_name = f"{department}-{random_string}"

        print(f"EC2 Instance {i+1} Name: {ec2_name}")

# Execute the function
generate_ec2_names()