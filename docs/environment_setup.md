# Python Utilities Project

This repository contains Python utilities for various integrations and core functionality. Below are instructions for setting up the development environment and running scripts.

## Development Environment Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python_templates.git
   cd python_templates
   ```

2. Install required dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

3. Set the `PYTHONPATH` environment variable to include the `src` directory:
   ```bash
   export PYTHONPATH=/Users/paulfry/git/python/python_templates/src
   ```
   Adding this ensures that Python can resolve imports correctly when running scripts directly.

   To make this permanent, add the export command to your shell configuration file:
   - For bash: `~/.bashrc` or `~/.bash_profile`
   - For zsh: `~/.zshrc`

   Example:
   ```bash
   echo "export PYTHONPATH=/Users/paulfry/git/python/python_templates/src" >> ~/.bashrc
   source ~/.bashrc
   ```

## Running Scripts

1. Navigate to the desired script directory or provide the full path to the script.
2. Ensure that the `PYTHONPATH` environment variable is set (see above).
3. Run the script using Python 3:
   ```bash
   python3 src/python_utils/classes/integrations/azure_key_vault/azure_key_vault_client.py
   ```

   If you prefer, you can create a shell script to simplify this process. For example:
   ```bash
   #!/bin/bash
   export PYTHONPATH=/Users/paulfry/git/python/python_templates/src
   python3 src/python_utils/classes/integrations/azure_key_vault/azure_key_vault_client.py
   ```

   Save this file as `run_client.sh`, make it executable, and run it:
   ```bash
   chmod +x run_client.sh
   ./run_client.sh
   ```

## Additional Documentation

Refer to the `docs` directory for more detailed information on project components and usage guidelines.
