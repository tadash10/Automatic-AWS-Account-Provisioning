# Automatic-AWS-Account-Provisioning



## Overview

The AWS Account Provisioning Script automates the creation of AWS accounts, IAM roles, and associated resources based on user-defined parameters. It promotes modularity, security best practices, and includes optional features with cautious guidance.

## Features

- **AWS Account Provisioning:**
  - Create AWS accounts with specified details such as email, account name, and IAM role.
  - Assign IAM roles and permissions following the principle of least privilege.
  - Notify users about the newly created AWS accounts.

- **Security Auditing:**
  - Log security events such as account creation and IAM role assignment for auditing purposes.
  - Enhance visibility into provisioning activities for security monitoring.

- **Optional Features:**
  - Integrate with identity providers for streamlined authentication and access management.
  - Use optional features with clear guidance to prevent unintended consequences.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/aws-account-provisioning.git

Navigate to the project directory:

bash

cd aws-account-provisioning

Install dependencies:

bash

    pip install -r requirements.txt

Usage
Provision AWS Accounts

bash

python main_script.py

    Replace John Doe with the DevSecOps professional's name.
    Modify num_accounts, account_names, regions, and iam_roles arrays as needed.

Use Optional Features

bash

python optional_features.py

    Execute the optional features script with caution, understanding the potential impact.

Security Auditing

Security auditing events are logged to provisioning_log.txt for auditing purposes.
Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements.
Certainly! Below is an example of a professional standard README file for your script. Please note that you may need to adapt it based on specific details or conventions followed in your organization.

markdown

# AWS Account Provisioning Script

## Overview

The AWS Account Provisioning Script automates the creation of AWS accounts, IAM roles, and associated resources based on user-defined parameters. It promotes modularity, security best practices, and includes optional features with cautious guidance.

## Features

- **AWS Account Provisioning:**
  - Create AWS accounts with specified details such as email, account name, and IAM role.
  - Assign IAM roles and permissions following the principle of least privilege.
  - Notify users about the newly created AWS accounts.

- **Security Auditing:**
  - Log security events such as account creation and IAM role assignment for auditing purposes.
  - Enhance visibility into provisioning activities for security monitoring.

- **Optional Features:**
  - Integrate with identity providers for streamlined authentication and access management.
  - Use optional features with clear guidance to prevent unintended consequences.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/aws-account-provisioning.git

    Navigate to the project directory:

    bash

cd aws-account-provisioning

Install dependencies:

bash

    pip install -r requirements.txt

Usage
Provision AWS Accounts

bash

python main_script.py

    Replace John Doe with the DevSecOps professional's name.
    Modify num_accounts, account_names, regions, and iam_roles arrays as needed.

Use Optional Features

bash

python optional_features.py

    Execute the optional features script with caution, understanding the potential impact.

Security Auditing

Security auditing events are logged to provisioning_log.txt for auditing purposes.
Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements.
License

This project is licensed under the MIT License.
