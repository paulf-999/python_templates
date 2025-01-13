<p align="center">
 <h1 align="center">Template Python Git Repo</h1>
</p>
<p align="center">
 <a href="https://github.com/psf/black">
 <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="black"/>
 </a>
 <a href="https://github.com/pre-commit/pre-commit">
 <img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="black"/>
 </a>
</p>

This repository offers a structured starting point for Python development, aimed to streamline & standardize Python projects at Payroc.

## 1. How Do I Use This Template Repo?

Expand the menu below for more details:

<details>

<summary>Click to expand</summary>

1. Click *"Use this template"* on GitHub.com to create a Git repo using this template.
2. Clone your new repo on your local machine
3. And start developing your Python project!

For more details, see [Github's instructions on how to create a repo from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
</details>

Once you've created your git repo using this template:

1. Rename `src/my_project/` to the name of your application.
2. Install `pre-commit` by running the command `pre-commit install`.
3. Update this `README`.

## 2. Coding Standards/Style Guide

See [docs/python_style_guide.md](docs/python_style_guide.md) for guidelines on writing clean and maintainable Python code.

## 3. Python Standards Checklist

To ensure code quality & maintainability, the Python standards checklist below should be used during code reviews and development, covering the themes of:

1. **Coding standards**
2. **Configuration**
3. **Error handling**
4. **Testing**
5. **Documentation**

Expand the menu below for more details:

<details>

<summary>Click to expand</summary>

1. **Coding Standards:**

    Verify adherence to [Payroc's Python coding standards](https://payroc.atlassian.net/wiki/spaces/TEC/pages/2544467994/Python+-+Standard+-+Style+Guide+Coding+Standards), in particualr:

   - [ ] Ensure adherence to PEP 8 guidelines.
   - [ ] Check for clear and meaningful variable/function names.
   - [ ] Verify consistent code formatting.

2. **Configuration:**
   - [ ] Ensure that the code is designed to be config-driven where appropriate.
   - [ ] Verify that configurable parameters are clearly defined and documented.
   - [ ] Check for separation of configuration from code logic.

3. **Error Handling:**
   - [ ] Check for proper implementation of error handling mechanisms.
   - [ ] Verify logging of errors for debugging and monitoring.
   - [ ] Ensure user-facing error messages are informative and helpful.

4. **Testing:**
   - [ ] Confirm the presence of unit tests for new/modified code.
   - [ ] Review test coverage for critical functionality.
   - [ ] Check for appropriate test assertions and coverage of edge cases.

5. **Documentation:**
   - [ ] Validate the presence of README updates, if applicable.
   - [ ] Ensure documentation of new dependencies or usage instructions.
   - [ ] Look for inline comments explaining complex logic or design decisions.

</details>

## 4. Setting Up a Virtual Environment

Setting up a virtual environment is a recommended practice to isolate project dependencies and avoid conflicts with other projects.

For detailed instructions, see [Setting Up a Virtual Environment](docs/virtualenv_setup.md).

## 6. Help

### `Python`

| Question                           | Answer |
| --------------------------------- | ----------- |
| What is the Python Project Structure? | See [How I should structure my Python project \| Confluence](https://payroc.atlassian.net/wiki/spaces/TEC/pages/2517270862/How+should+I+structure+my+Python+project+source+directories+for+package+distribution). |
| How do I setup a virtual environment? | See [Setting Up a Virtual Environment](docs/virtualenv_setup.md). |

### `pre-commit`

| Question                           | Answer |
| --------------------------------- | ----------- |
| What is `pre-commit`? | See [What is pre-commit? \| Confluence](https://payroc.atlassian.net/wiki/spaces/DA/pages/2938273870/What+is+pre-commit). |
| How do you install & use `pre-commit`? | See [How-to: Set up pre-commit? \| Confluence](https://payroc.atlassian.net/wiki/spaces/DA/pages/2414313478/How-to+Set+up+pre-commit). |
