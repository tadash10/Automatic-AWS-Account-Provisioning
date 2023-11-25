# security_auditing.py
import logging

# Configure logging
logging.basicConfig(filename='security_audit.log', level=logging.INFO)

def log_security_event(event_type, details):
    """
    Log security events for auditing purposes.
    
    Parameters:
    - event_type (str): Type of security event (e.g., 'AccountCreation', 'IAMRoleAssignment').
    - details (dict): Details about the security event.
    """
    log_message = f"{event_type}: {details}"
    logging.info(log_message)


def account_creation_audit(account_name, account_id, region):
    """
    Log details about AWS account creation for auditing purposes.
    
    Parameters:
    - account_name (str): Name of the newly created AWS account.
    - account_id (str): ID of the newly created AWS account.
    - region (str): AWS region where the account is created.
    """
    event_type = 'AccountCreation'
    details = {'AccountName': account_name, 'AccountID': account_id, 'Region': region}
    log_security_event(event_type, details)


def iam_role_assignment_audit(account_id, iam_role):
    """
    Log details about IAM role assignment for auditing purposes.
    
    Parameters:
    - account_id (str): ID of the AWS account where the IAM role is assigned.
    - iam_role (str): Name of the IAM role assigned.
    """
    event_type = 'IAMRoleAssignment'
    details = {'AccountID': account_id, 'IAMRole': iam_role}
    log_security_event(event_type, details)
