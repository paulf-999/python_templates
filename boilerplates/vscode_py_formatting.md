# Python linting settings in VSCode

In VSCode, go to:

Preferences -> Settings (shortcut: `cmd+,`) then select the icon in the top right "Open Settings (JSON)".

Following this, paste the following inside the outer curly brackets:

```
"python.linting.flake8Enabled": true,
"python.linting.banditEnabled": true,
"python.linting.pylintEnabled": true,
"python.linting.flake8Args": [
    "--max-line-length=200",
    "--extend-ignore=F401"
],
"files.trimTrailingWhitespace": true,
"python.formatting.provider": "black",
"python.formatting.blackArgs": [
    "--line-length",
    "200"
],
"python.formatting.blackPath": "black",
"[python]": {
    "editor.formatOnSave": true,
}
```
