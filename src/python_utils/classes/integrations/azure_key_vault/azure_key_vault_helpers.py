#!/usr/bin/env python3
"""
Description: A script to setup and interact with Azure Key Vault, including Key Vault client initialization.
Date created: 2024-08-08
"""
# flake8: noqa: E402

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv

# Custom modules
from python_utils.classes.core.logging_utils import LoggingUtils

# Initialize logging utilities
logging_utils = LoggingUtils()
logger = logging_utils.logger

# Load environment variables from .env file
load_dotenv()

# Constants
PY_SCRIPT_NAME = os.path.basename(__file__)


def get_azure_constructors():
    """Setup the Azure Key Vault client and URL."""
    logger.debug("Setting up Azure Key Vault client.")

    # store the function name as a constant
    FUNCTION_NAME = "get_azure_constructors"
    AZURE_VAULT_URL_ENV_VAR = "AZURE_VAULT_URL"

    # Retrieve the Key Vault URL from environment variables
    key_vault_url = os.getenv(AZURE_VAULT_URL_ENV_VAR)

    if not key_vault_url:
        # Log error and exit if the environment variable is missing
        error_msg = f"Required ENV VAR '{AZURE_VAULT_URL_ENV_VAR}' is missing."
        logging_utils.log_error(error_msg, PY_SCRIPT_NAME, FUNCTION_NAME, "EnvironmentError")
        sys.exit(1)

    try:
        # Initialize the Azure Key Vault client
        credential = DefaultAzureCredential()
        secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
        return secret_client, key_vault_url

    except Exception as e:
        # Log the exception and exit if an error occurs
        logging_utils.log_error(f"An error occurred: {str(e)}", PY_SCRIPT_NAME, FUNCTION_NAME, "Exception")
        sys.exit(1)


def list_secrets(secret_client, key_vault_url):
    """List the secrets stored in the Key Vault."""
    logger.info(f"Listing all secrets in the Key Vault '{key_vault_url}':\n")
    try:
        secrets = secret_client.list_properties_of_secrets()
        for secret in secrets:
            logger.info(f"Secret Name: {secret.name}")
        return secrets
    except Exception as e:
        logging_utils.log_error(str(e), PY_SCRIPT_NAME, "list_secrets", e)
        sys.exit(1)


def get_secret_value(secret_client, secret_name):
    """Retrieve the value of a secret from the Key Vault."""
    logger.info(f"Retrieving value for secret '{secret_name}':\n")
    try:
        secret_object = secret_client.get_secret(secret_name)
        logger.info(f"Secret: {secret_name}\nValue: {secret_object.value}")
        return secret_object.value
    except Exception as e:
        logging_utils.log_error(str(e), PY_SCRIPT_NAME, "get_secret_value", e)
        sys.exit(1)


def save_secret(secret_client, secret_name, secret_value):
    """Save a new secret to the Key Vault."""
    logger.info(f"Saving secret '{secret_name}' with provided value.")
    try:
        secret_client.set_secret(secret_name, secret_value)
    except Exception as e:
        logging_utils.log_error(str(e), PY_SCRIPT_NAME, "save_secret", e)
        sys.exit(1)


def delete_secret(secret_client, secret_name):
    """Delete a secret from the Key Vault."""
    logger.info(f"Deleting secret '{secret_name}':")
    try:
        poller = secret_client.begin_delete_secret(secret_name)
        deleted_secret = poller.result()
        return deleted_secret
    except Exception as e:
        logging_utils.log_error(str(e), PY_SCRIPT_NAME, "delete_secret", e)
        sys.exit(1)
