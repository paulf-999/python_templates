# Python linting settings in VSCode

In VSCode, go to:

Preferences -> Settings (shortcut: `cmd+,`) then select the icon in the top right "Open Settings (JSON)".

Following this, paste the following inside the outer curly brackets:

```
{
    "sync.autoUpload": true,
    "sync.forceUpload": true,
    "workbench.iconTheme": "vscode-icons",
    "sync.gist": "3619a9e90f0bdabd9859e91dc4848ef6",
    "workbench.startupEditor": "newUntitledFile",
    "workbench.colorCustomizations": {
    },
    "explorer.confirmDragAndDrop": false,
    "explorer.confirmDelete": false,
    "python.pythonPath": "/usr/local/bin/python3",
    "terminal.integrated.env.osx": {
        "PATH": "...:/usr/bin:/bin:..."
    },
    "workbench.editorAssociations": {
        "*.ipynb": "jupyter-notebook"
    },
    "editor.renderWhitespace": "all",
    "notebook.cellToolbarLocation": {
        "default": "right",
        "jupyter-notebook": "left"
    },
    "python.linting.flake8Enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Args": [
        "--extend-ignore=F401",
        "--max-line-length=200"
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
    },
    "security.workspace.trust.untrustedFiles": "open",
    "mssql.connections": [
        {
            "server": "{{put-server-name-here}}",
            "database": "{{put-database-name-here}}",
            "user": "{{put-username-here}}",
            "password": "{{put-password-here}}"
        }
    ],
    "[sql]": {
        "editor.defaultFormatter": "dorzey.vscode-sqlfluff"
    },
    "settingsSync.ignoredExtensions": [

    ],
    "sync.autoDownload": true,
    "sync.quietSync": true,
    "aws.profile": "profile:pf",
    "redhat.telemetry.enabled": false,
    "terminal.integrated.fontFamily": "MesloLGS NF",
    "todo-tree.general.tags": [
        "BUG",
        "HACK",
        "FIXME",
        "TODO",
        "XXX",
        "[ ]",
        "[x]"
    ],
    "todo-tree.regex.regex": "(//|#|<!--|;|/\\*|^|^\\s*(-|\\d+.))\\s*($TAGS)",
    "yaml.customTags": [
        "!And",
        "!And sequence",
        "!If",
        "!If sequence",
        "!Not",
        "!Not sequence",
        "!Equals",
        "!Equals sequence",
        "!Or",
        "!Or sequence",
        "!FindInMap",
        "!FindInMap sequence",
        "!Base64",
        "!Join",
        "!Join sequence",
        "!Cidr",
        "!Ref",
        "!Sub",
        "!Sub sequence",
        "!GetAtt",
        "!GetAZs",
        "!ImportValue",
        "!ImportValue sequence",
        "!Select",
        "!Select sequence",
        "!Split",
        "!Split sequence"
    ],
    "yaml.schemas": {},
    "json.schemas": [],
    "python.defaultInterpreterPath": "/usr/local/bin/python3",
    "editor.multiCursorModifier": "ctrlCmd",
    "tabnine.experimentalAutoImports": true,
    "GitLive.Issue tracker integration": "Disabled",
    "bracket-pair-colorizer-2.depreciation-notice": false,
    "editor.suggest.showMethods": true,
    "editor.suggest.preview": true,
    "editor.acceptSuggestionOnEnter": "on",
    "editor.snippetSuggestions": "top",
    "aws.suppressPrompts": {
        "regionAddAutomatically": true
    },
    "files.associations": {
        "*.sql": "jinja-sql"
    },
    "cSpell.language": "en-GB",
    "markdownlint.config": {
        "MD033": false,
        "MD037": false
    },
    "git.ignoredRepositories": [
        "/Users/paulfry/.vscode/extensions/stepsize.stepsize-0.63.0/resources/demo-repository"
    ]
}
```
