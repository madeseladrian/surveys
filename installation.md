# Installation

## > Git 
```git init```

### > Change the branch nam
```git branch -m main```

### > Create .gitignore
```
**/__pycache__
.venv
.env
```

### > Create .env example
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=27017
DATABASE_USERNAME=mades
DATABASE_PASSWORD=123456
SECRET_KEY = "19d25e094faa5aa2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30
```

## Install pdm (Version control)
```pdm init```

## > Install pre-commit
```pdm add --dev pre-commit```

### > Add pre-commit config: .pre-commit-config.yaml
```
repos:
-   repo: local
    hooks:      
      - id: requirements
        name: requirements
        entry: bash -c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

### > Run the command to activate pre-commit
```
pdm run pre-commit install
```

### > First commit
```git c "add pre-commit"```

### > Active the environment
```
source venv/Scripts/activate (Bash)
.venv\Scripts\activate       (Windows)
``` 

## > Install mypy
```pdm add --dev mypy```

### > Install vscode extension mypy and sourcery

### > Create a config mypy.ini 
```
[mypy]
exclude='.venv'
ignore_missing_imports = True
ignore_missing_imports_per_module = True
```

### Configuration settings.json: Use inside the environment
```
"[python]": {
    "editor.tabSize": 4
},
"mypy.runUsingActiveInterpreter": true,
```

### > Add pre-commit config: .pre-commit-config.yaml
```
repos:
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.982
    hooks:
      - id: mypy
        files: ^src/
        args: []

-   repo: local
    hooks:      
      - id: requirements
        name: requirements
        entry: bash -c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

## > Install flake8
```pdm add --dev flake8```

### > Add flake8 config: .flake8
```
[flake8]
ignore=
  # 2 blank lines
  E302
  # 2 blank lines after class or function definition
  E305
  # indentation is not a multiple of 4
  E111
  # indentation is not a multiple of 4 (comment)
  E114
  # continuation line under-indented for hanging indent
  E121
  # line too long (84 > 79 characters)
  E501
  
# imported but unused
per-file-ignores =
    __init__.py: F401
```

### Configuration settings.json
```
"python.linting.flake8Enabled": true,
```

### > Add pre-commit config: .pre-commit-config.yaml
```
repos:
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.971
    hooks:
      - id: mypy
        files: ^src/
        args: []

-   repo: https://gitlab.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    - id: flake8
      language: python 

-   repo: local
    hooks:
      - id: requirements
        name: requirements
        entry: bash -c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

## > Install pytest
```
pdm add --dev pytest
pdm add --dev pytest-cov
```

### > Create pytest.ini
```
[pytest]
testpaths = tests
addopts = --cov --cov-report=html
```

### > Install the extension: 
```Python Test Explorer for Visual Studio Code - Little Fox Team```

### > Configuration setttings.json
```
// these settings are 'false' by default, so removing those should also work
"python.testing.unittestEnabled": true,
"python.testing.pytestEnabled": true,
"pythonTestExplorer.testFramework": "pytest" // (or unittest)
```

### > Add pre-commit config: .pre-commit-config.yaml
```
repos:
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.971
    hooks:
      - id: mypy
        files: ^src/
        args: []

-   repo: https://gitlab.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    - id: flake8
      language: python 

-   repo: local
    hooks:
      - id: pytest-check
        name: pytest-check
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
        stages: [commit]

      - id: pytest-coverage
        name: pytest-coverage
        entry: bash -c 'pytest --cov --cov-report=html; git add .'
        language: system
        pass_filenames: false
        always_run: true
        stages: [commit]
      
      - id: requirements
        name: requirements
        entry: bash -c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]

```

### > Install Pydocstyle
```pdm add --dev pydocstyle```

### > Create .pydocstyle.ini
```
[pydocstyle]
ignore = D100, D202, D203, D208, D213
match='(?!test_).*\.py
```

### > Install the extension: 
```autoDocstring - Python Docstring Generator - Nils Werner```

### > Configuration setttings.json
```
"autoDocstring.docstringFormat": "one-line-sphinx"
```

### > Add pre-commit config: .pre-commit-config.yaml
```
repos:
-   repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.971
    hooks:
      - id: mypy
        files: ^src/
        args: []

-   repo: https://gitlab.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    - id: flake8
      language: python 

-   repo: https://github.com/pycqa/pydocstyle
    rev: 6.1.1
    hooks:
    -   id: pydocstyle  

-   repo: local
    hooks:
      - id: pytest-check
        name: pytest-check
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
        stages: [commit]

      - id: pytest-coverage
        name: pytest-coverage
        entry: bash -c 'pytest --cov --cov-report=html; git add .'
        language: system
        pass_filenames: false
        always_run: true
        stages: [commit]
      
      - id: requirements
        name: requirements
        entry: bash -c 'pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```
