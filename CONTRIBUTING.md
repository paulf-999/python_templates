# Contributing Guidelines

Thanks for contributing to **Python Utilities Project**! Please follow these conventions to keep the project consistent.

---

## Branching

* Branch from `develop` (or `main` if no `develop`).
* Use descriptive names:

  * `feature/<name>` – new features
  * `bugfix/<name>` – fixes
  * `hotfix/<name>` – urgent patches
  * `release/<version>` – release prep

Example:

```bash
git checkout -b feature/add-snowflake-utils
```

---

## Commits

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(scope): <short description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

Examples:

```bash
feat: add Azure Key Vault client
fix: correct variable utils import path
docs: update environment setup guide
```

---

## Code & Tests

* Follow the [Python Style Guide](docs/python_style_guide.md).
* Add/maintain tests in `src/tests/`.
* Run before PRs:

  ```bash
  pytest src/tests/
  ```

---

## Pull Requests

* Keep PRs focused and small.
* Ensure tests pass and code follows style guide.
* At least one reviewer approval required.

### ✅ PR Checklist

* [ ] Branch follows naming conventions
* [ ] Commits use Conventional Commits format
* [ ] Tests added/updated and passing
* [ ] Code follows [Python Style Guide](docs/python_style_guide.md)
* [ ] Documentation updated if needed
