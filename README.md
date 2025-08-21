# Python Utilities Project

Reusable Python utilities for **core functionality** and **integrations** (Snowflake, Azure Key Vault, Jinja, logging, variables). Includes examples, documentation, and tests to support consistent development.

---

## Contents

1. Summary
2. Getting Started

   * Prerequisites
   * Installation
   * How-to Run
3. Git Branching Strategy
4. Help
5. Folder Contents

---

## 1. Summary

This project provides a structured set of **Python utilities and templates** to accelerate development.
It covers core utilities, integrations, examples, and coding standards.

### Technologies Used

* Python 3
* Pytest
* Azure Key Vault
* Snowflake
* Jinja2

---

## 2. Getting Started

### Prerequisites

* Python 3.8+ and pip
* Git

### Installation

```bash
git clone https://github.com/yourusername/python_templates.git
cd python_templates
pip install -r requirements.txt
```

Set `PYTHONPATH`:

```bash
export PYTHONPATH=/path/to/python_templates/src
```

### How-to Run

Run scripts directly:

```bash
python3 src/python_utils/classes/integrations/azure_key_vault/azure_key_vault_client.py
```

Run tests:

```bash
pytest src/tests/
```

---

## 3. Git Branching Strategy

See [docs/git\_branching\_strategy.md](docs/git_branching_strategy.md).

---

## 4. Help

* **Import errors** → check `PYTHONPATH`
* **Dependencies missing** → `pip install -r requirements.txt --upgrade`
* **Code style** → follow [Python Style Guide](docs/python_style_guide.md)

---

## 5. Folder Contents

| Path                                     | Description                                      |
| ---------------------------------------- | ------------------------------------------------ |
| `examples/`                              | Example scripts                                  |
| `src/python_utils/classes/core/`         | Core utilities (file, logging, variables)        |
| `src/python_utils/classes/integrations/` | Integrations (Azure Key Vault, Snowflake, Jinja) |
| `src/tests/`                             | Unit tests                                       |
