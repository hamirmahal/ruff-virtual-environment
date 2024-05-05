# Setup

1.  Run

```
du -sh . && python3 -m venv venv/ && du -sh .
```

2. Restart your terminal or run

```
source venv/bin/activate
```

## To install the packages in [`requirements.txt`](requirements.txt)

```
pip list && echo && du -sh .
pip install -r requirements.txt && echo && pip list && echo && du -sh .
```

## To install the latest packages

```
pip list && echo && du -sh .
pip install ruff && echo && pip list && echo && du -sh .
pip install mypy && echo && pip list && echo && du -sh .
pip install pre-commit && echo && pip list && echo && du -sh .

# "Freeze" the requirements so we know what versions we are using.
pip freeze > requirements.txt && pip list
```

## Pre-commit

Run

```
du -sh . && pre-commit install && du -sh .
```

to setup pre-commit hooks.

# Testing, Type Checking, Formatting and Linting

1. Run

```
./s.sh
```

# Running the Program

You can run the program with

```
time python src/main.py
```

in your terminal after completing setup.
