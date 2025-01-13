# Azure Key Vault Client Scripts

* These scripts are intended to help developers manage secrets in Azure Key Vault via command-line operations.
* The main script (`azure_key_vault_client.py`) serves as the entry point and can execute various commands related to Azure Key Vault secrets.

## 1. Prerequisites

Before running these scripts, ensure that you have the following prerequisites met:

<details>

<summary>Expand for more details</summary>

1. **Azure CLI**: Install the [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) and authenticate using the command `az login`.
2. **Environment Variables**:

    Create a `.env` file in the root directory containing the environment variable `AZURE_VAULT_URL` with your Azure Key Vault URL.

3. **Dependencies**: Install the required Python packages by running: `pip install -r requirements.txt`

   Your `requirements.txt` should include:

   <details>

    <summary>Expand for more details</summary>
   - `azure-identity`
   - `azure-keyvault-secrets`
   - `python-dotenv`

   These packages are required to interact with Azure Key Vault and manage environment variables.
    </details><br/>

4. **Authentication**: Before running the script, authenticate with Azure using:

   ```bash
   az login
   ```

</details>

## 2. Usage

### General Usage

To run the script, use the following command structure: `python3 azure_key_vault_client.py <command> [arguments]`

### Commands

| Command                              | Description                                                | Example Command                                                       |
|--------------------------------------|------------------------------------------------------------|------------------------------------------------------------------------|
| **`list_secrets`**                   | Lists all secrets in the Azure Key Vault.                  | `python3 azure_key_vault_client.py list_secrets`                       |
| **`get_secret_value <secret_name>`** | Retrieves the value of a specified secret.                 | `python3 azure_key_vault_client.py get_secret_value <secret_name>`     |
| **`save_secret <secret_name> <secret_value>`** | Saves or updates a secret in Azure Key Vault.        | `python3 azure_key_vault_client.py save_secret <secret_name> <secret_value>` |
| **`delete_secret <secret_name>`**    | Deletes a specified secret from Azure Key Vault.           | `python3 azure_key_vault_client.py delete_secret <secret_name>`        |
