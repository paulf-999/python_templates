#!/usr/bin/env python3
"""
Python Version  : 3.9
* Name          : azure_key_vault_client.py
* Description   : Generic script for interacting with Azure Key Vault.
*               : Note - you will need to run `az login` prior to running this script.
*               : I.e., the script is script is intended to be used with the Azure CLI tool.

*               : This script follows the instructions described in the link below:
*                 https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli#authenticate-and-create-a-client
* Created       : 01-06-2023
* Usage         : python3 azure_key_vault_client.py
*               : Prerequisite: this script is intended to be used with the Azure CLI tool.
*               : I.e., you will need to run `az login` prior to running this script.
"""

__author__ = "Paul Fry"
__version__ = "1.0"

import os
import sys
import logging

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from dotenv import load_dotenv


# Set up a specific logger with our desired output level"""
logging.basicConfig(format="%(message)s")
logger = logging.getLogger("application_logger")
logger.setLevel(logging.INFO)


def list_secrets(secret_client):
    """List the secrets stored within the input Key Vault URL"""

    logger.info("Function called: 'list_secrets()'. List the secrets stored within the input Key Vault URL.")

    # store the secrets within the input KV within a list
    secrets = secret_client.list_properties_of_secrets()

    return secrets


def get_secret_value(secret_client, secret_name):
    """Return the value of a Key Vault secret"""

    logger.info("Function called: 'get_secret_value()'. Return the value of a Key Vault secret.")

    # store the secret value in a var
    secret_object = secret_client.get_secret(secret_name)

    return secret_object.value


def save_secret(secret_client, secret_name, secret_value):
    """Add a new secret to the Azure Key Vault"""

    logger.info("Function called: 'save_secret()'. Add a new secret to the Azure Key Vault.")

    secret_client.set_secret(secret_name, secret_value)

    return


def delete_secret(secret_client, secret_name):
    """Delete a secret from an input Azure Key Vault"""

    logger.info("Function called: 'delete_secret()'. Delete a secret from an input Azure Key Vault")

    poller = secret_client.begin_delete_secret(secret_name)
    deleted_secret = poller.result()

    return deleted_secret


def main(input_arg):
    """Orchestration logic of the script"""

    if input_arg == "list_secrets":
        secrets = list_secrets(secret_client)

        logger.info(f"\nList all secrets stored in the input key vault URL '{key_vault_url}':\n")
        for secret in secrets:
            logger.info(secret.name)

    elif input_arg == "get_secret_value":
        validate_inputs(env_vars=["AZURE_SECRET_NAME"])

        secret_name = os.environ.get("AZURE_SECRET_NAME")
        secret_value = get_secret_value(secret_client, secret_name=secret_name)

        logger.info(f"\nSecret:\t{secret_name}\nValue:\t{secret_value}")

    elif input_arg == "save_secret":
        validate_inputs(env_vars=["AZURE_SECRET_NAME", "AZURE_SECRET_VALUE"])

        save_secret(
            secret_client,
            secret_name=os.environ.get("AZURE_SECRET_NAME"),
            secret_value=os.environ.get("AZURE_SECRET_VALUE"),
        )

    else:
        logger.error("\nERROR: Invalid input arg provided.")
        logger.info("\nUsage: python3 azure_key_vault_client.py [azure function to call here]")
        logger.info("\nOptions: \n* list_secrets \n* get_secret_value \n* save_secret")
        sys.exit()

    return


def validate_inputs(env_vars):
    """Validate the user's input values"""

    for env_var in env_vars:
        if os.getenv(env_var) is None:
            logger.info("\n###########################################################")
            logger.error(f"# ERROR: Required ENV VAR '{env_var}' is missing.")
            logger.info("###########################################################")
            sys.exit()

    return


def create_az_secret_client():
    """Create Azure Secret Client"""
    load_dotenv()

    # Prerequisite: ENV VAR called 'AZURE_VAULT_URL'. This is used to store the name of the input Key Vault.
    # For example: `https://<your_keyvault_name>.vault.azure.net`.
    if os.getenv("AZURE_VAULT_URL") is not None:
        key_vault_url = os.environ.get("AZURE_VAULT_URL")

        # The `DefaultAzureCredential` class is the recommended approach for implementing password-less connections to Azure services.
        # See: https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli#authenticate-and-create-a-client
        credential = DefaultAzureCredential()

        # The SecretClient class provides methods to manage Secrets inside an Azure Key Vault.
        secret_client = SecretClient(vault_url=key_vault_url, credential=credential)
    else:
        logger.error("\nERROR: Required ENV VAR 'AZURE_VAULT_URL' is missing.")
        logger.info("\nExample: AZURE_VAULT_URL=https://<YOUR_KEY_VAULT_NAME>.vault.azure.net")
        sys.exit()

    return secret_client, key_vault_url


if __name__ == "__main__":
    """This is executed when run from the command line"""

    # Note: This script requires an ENV VAR called 'AZURE_VAULT_URL'. This is used to store the name of the input Key Vault.
    # For example, AZURE_VAULT_URL=https://<your_keyvault_name>.vault.azure.net
    secret_client, key_vault_url = create_az_secret_client()

    # validate the command line input
    if len(sys.argv) < 2:
        logger.info("\n############################################################################")
        logger.info("# ERROR: No input arguments provided.")
        logger.info("#\n# Usage: python3 azure_key_vault_client.py [azure function to call here]")
        logger.info("############################################################################")
    else:
        # orchestrate the python function to call
        main(input_arg=sys.argv[1])
