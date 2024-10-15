create database Insurance_Management_System;
use Insurance_Management_System;

-- Keeping reserved keyword in mind, delimiting it by []
CREATE TABLE [User] (
    user_id INT PRIMARY KEY,
    user_name NVARCHAR(255),
    user_password NVARCHAR(255),
    user_role NVARCHAR(50)
);

CREATE TABLE [Policy] (
    policy_id INT PRIMARY KEY,
    policy_name NVARCHAR(255),
    premium_cost DECIMAL(10, 2),
    coverage_limit DECIMAL(10, 2)
);

CREATE TABLE Claim (
    claim_id INT PRIMARY KEY,
    claim_num NVARCHAR(255),
    file_date DATETIME,
    amount DECIMAL(10, 2),
    claim_status NVARCHAR(50),
    policy_id INT,
    customer_id INT,
    FOREIGN KEY (policy_id) REFERENCES Policy(policy_id)
);

CREATE TABLE Client (
    customer_id INT PRIMARY KEY,
    customer_name NVARCHAR(255),
    contact_details NVARCHAR(255),
    policy_ref INT,
    FOREIGN KEY (policy_ref) REFERENCES Policy(policy_id)
);

CREATE TABLE Payment (
    transaction_id INT PRIMARY KEY,
    transaction_date DATETIME,
    transaction_amount DECIMAL(10, 2),
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES Client(customer_id)
);










