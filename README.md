# Python Templates

Python template scripts I've collated over time, as described below.

## Python Style Guide

Throughout the template scripts developed, the following style guide of do’s and don’ts for Python development has been used, covering the following main areas:

1. Naming Conventions
2. Code Layout
3. String Formatting: Use f-strings
4. Function and Method Definitions
5. Comments and Docstrings
6. Error Handling
7. General Guidelines

---

## 1. Naming Conventions

### 1.1. Case Styles, Per-Python Object

In summary:

1. Use `snake_case` for all module, package, function, and variable names.
2. Use `CamelCase` for classes.
3. Use `SCREAMING_SNAKE_CASE` for constants.

**What is snake_case?**
Expand the menu below for more details.

<details>
<summary>Expand for details</summary>

`snake_case` combines words by replacing each space with an underscore (_), and all letters are lowercase, as follows:

**Raw**: user login count

**Snake case**: user_login_count

- [The following link](https://betterprogramming.pub/string-case-styles-camel-pascal-snake-and-kebab-case-981407998841) explains the differences between different case styles.
- One of the benefits of `snake_case` is that many of the allowed characters are compatible across S3 and Snowflake.

</details>

#### Case Style Specification

<details>
<summary>Expand for details</summary>

| Related to                 | Naming Convention                                     | Example                          |
|---------------------------|-------------------------------------------------------|----------------------------------|
| 1. Module names           | `snake_case` (i.e., `lowercase_with_underscores`)         | `lowercase_with_underscores.py`    |
| 2. Package names          | `snake_case`                                            | `lowercase_with_underscores`       |
| 3. Class names            | `CamelCase`                                             | `ExampleClass`                     |
| 4. Function and method names | `snake_case`                                           | `def example_function():`         |
| 5. Variable names         | `snake_case`                                            | `working_dir = os.getcwd()`        |
| 6. Constants              | `SCREAMING_SNAKE_CASE` (i.e., `UPPERCASE_WITH_UNDERSCORES`) | `PI = 3.14`                        |
</details>

### 1.2. Avoid Abbreviations

- Function names, variables, and filenames should all be meaningful, descriptive, and eschew abbreviations.

    <details>
    <summary>For example (click to expand)</summary>
    Good:

    ```python
    def load_customer_data():
    ```

    Bad:

    ```python
    def load_data():
    ```

    </details>

- Don't use abbreviations that are ambiguous to readers outside your projects.
- Don't abbreviate by deleting letters within a word.

---

## 2. Code Layout

### 2.1. General

[PEP 8 is the official style guide for Python code](https://peps.python.org/pep-0008/). It provides a set of conventions for writing readable and consistent code. As such, we should use its main high-level code layout recommendations, listed below:

- Using four spaces for indentation
- Limiting lines to 79 characters
- Using blank lines to separate functions and classes

Expand the menu below for further details on these (including examples).

<details>
<summary>Example (click to expand)</summary>

#### Indentation

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Use four spaces for indentation (i.e., avoid tabs.)                     | N/A                                                                 |

#### Line length

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Limit lines to a maximum of 79 characters.                              | N/A                                                                 |

#### Whitespace: imports, classes, and functions

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Use a newline after imports and before the class or function definition. | Expand menu below                                                |

<details>
<summary>Example (click to expand)</summary>

Good

```python
import os
...

from requests import HTTPError


def example_function():

```

Bad

```python
import os
...

from requests import HTTPError
def example_function():

```

</details>

#### Whitespace: methods and classes

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Separate methods and classes with two blank lines.                      | Expand menu below                                                 |

<details>
<summary>Example (click to expand)</summary>

Good

```python

import os
...

from requests import HTTPError


def example_function():

```

Bad

```python

import os
...

from requests import HTTPError
def example_function():

```

</details>

#### Whitespace: operators and commas

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Use a single space around operators and after commas.                   | Expand menu below                                                 |

<details>
<summary>Example (click to expand)</summary>

Good

```python
return sharepoint.get_site(host, 'sites/' + site_name.replace(" ", ""))
```

Bad

```python
return sharepoint.get_site(host,'sites/'+site_name.replace(" ", ""))
```

</details>

#### Whitespace: code readability

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Code MUST be spaced logically to maintain readability.                  | Expand menu below                                                 |

<details>
<summary>Example (click to expand)</summary>

Good

```python
# Pipeline parameters
src_bucket = self.s3_bucket_src
logging.info(f”source_bucket = {src_bucket}”)

target_bucket = self.s3_bucket_target
logging.info(f”target_bucket = {target_bucket}”)
```

Bad

```python
# Pipeline parameters
src_bucket = self.s3_bucket_src
logging.info(f”source_bucket = {src_bucket}”)
target_bucket = self.s3_bucket_target
logging.info(f”target_bucket = {target_bucket}”)
```

</details>
</details>

### 2.2. Imports

- Import modules on separate lines.
- Use absolute imports whenever possible.
- Avoid wildcard imports (`from module import *`).
- Place imports in the following order: standard library modules, third-party modules, and local modules.

For further details (with examples), expand the menu below.

<details>
<summary>Click to expand</summary>

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Import modules on separate lines.                  | Expand menu below                                                 |

<details>
<summary>Click to expand</summary>

Good

```python
import os
import re
```

Bad

```python
import os, re
```

</details>

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Use absolute imports whenever possible.                  | Expand menu below                                                 |

<details>
<summary>Click to expand</summary>

Good

```python
from package2.subpackage1.module5 import function2
```

Bad

```python
from .subpackage1.module5 import function2
```

</details>

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Avoid wildcard imports (`from module import *`)                  | Expand menu below                                                 |

<details>
<summary>Click to expand</summary>

Good

```python
from math import ceil
```

Bad

```python
from math import *
```

</details>

| Description                                                             | Example                                                           |
|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| Place imports in the following order:<br/>1. standard library modules,<br/>2. third-party modules,<br/>3. and local modules.| Expand menu below                                                 |

<details>
<summary>Click to expand</summary>

Good

```python
import os # standard modules
import boto3 # third-party modules
import my_local_module # local modules
```

Bad

```python
import boto3 # third-party modules
import my_local_module # local modules
import os # standard modules
```

</details>

</details>

---

## 3. String Formatting: Use `f-strings`

- `f-strings` should be used where possible. They provide a clean way to format strings.
- Avoid using `str().format`.
- Detailed examples of `f-strings` in action can be found [here](https://realpython.com/python-f-strings/).

---

## 4. Function and Method Definitions

- Use type declarations for method arguments and return values.

    <details>
    <summary>Click to expand</summary>

    Good

    ```python
    def get_secret_by_name(secret_name: str) -> str:

    ...

    secret = <code here>

    return secret
    ```

    Bad

    ```python
    def get_secret_by_name(secret_name):

    ...

    secret = <code here>

    return s
    ```

    </details>

- Place default arguments at the end of the argument list.

    <details>
    <summary>Click to expand</summary>

    Good

    ```python
    def student(firstname, lastname ='Mark', standard ='Fifth'):
    ```

    Bad

    ```python
    def student(lastname ='Mark', standard ='Fifth', firstname):
    ```

    </details>

- Define function parameters without spaces around the equals sign.

    <details>
    <summary>Click to expand</summary>
    Good

    ```python
    func(1, 2, axis='x', angle=90, size=450, name='foo bar')
    ```

    Bad

    ```python
    func(1, 2, axis = 'x', angle = 90, size = 450, name = 'foo bar')
    ```

    </details>

- Use a single space after the comma in function definitions.

    <details>
    <summary>Click to expand</summary>

    Good

    ```python
    func(1, 2, axis='x', angle=90, size=450, name='foo bar')
    ```

    Bad

    ```python
    func(1,2,axis='x',angle=90,size=450,name='foo bar')
    ```

    </details>

---

## 5. Comments and Docstrings

### 5.1. Comments

- Use inline comments sparingly and keep them concise.
- Use docstrings to document modules, classes, methods, and functions.
- Write clear, self-explanatory code and minimize the need for comments.

#### Don't Capture Change History/Log

<details>
<summary>Expand for more details</summary>

- The change history SHOULD NOT be stored in the code itself.
- Manually maintaining the change history in the code itself is unreliable, as it doesn't show the actual change that has occurred and isn't enforceable.
  - The change history is captured by the version control system (e.g., Git) for each commit that's occurred. All changes that are pushed to development and production are captured, and diffs between those changes are available.
- An example of the anti-pattern that SHOULD NOT be used:

```python
# Created by: Joe Bloggs
# Date: 01-01-2021
# Purpose: Eg transformation script

# Change log
# Date: 02-01-2021
# Change Made By: Donald Duck
# Change Description: Small change to JSON file read in
```

</details>

### 5.2. Docstring

All functions should start with a Docstring, explaining **the function, what it does, and why**.

#### DocString Format: Use reST

Use the reST (restructuredText) Docstring format.

**What is the reST (restructuredText) Docstring format?**

Expand the menu below for more details.

<details>
<summary>Click to expand</summary>
One of the most prevalent Docstring formats today is reST (restructuredText).
Shown below are the main components of the reST Docstring format:

```python
"""[Summary]
:param [ParamName]: [ParamDescription], defaults to [DefaultParamVal]
:type [ParamName]: [ParamType](, optional)
...
:raises [ErrorType]: [ErrorDescription]
...
:return: [ReturnDescription]
:rtype: [ReturnType]
"""
```

- For an overview of the reST Docstring format, see here.
- The main components of the reST Docstring format are described below.

</details>

---

## 6. Error Handling

- Prefer specific exceptions over catching all exceptions (`except Exception:`).
- Use `try-except-else` blocks when possible.
- Use `finally` blocks sparingly and only when necessary.

## 7. General Guidelines

- Failing all of the above, [follow the PEP 8 guidelines](https://peps.python.org/pep-0008/) for conventions not covered here.
- For additional inspiration, refer to the [Google Python style guide](https://google.github.io/styleguide/pyguide.html) for great examples of do's and don'ts on writing clean Python code.
- Remember, consistency is key when it comes to style guides. Following the established style within a project or organization is essential to maintain code readability and maintainability.
