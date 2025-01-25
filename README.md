# Setup

1.  Run

```
python3 -m venv venv/
```

2. Restart your terminal or run

```
source venv/bin/activate
```

## To install the packages in [`requirements.txt`](requirements.txt)

```
pip list
pip install -r requirements.txt
pip list
pre-commit install
pip list
```

## To install the latest packages

```
pip list
pip install ruff
pip list
pip install mypy
pip list
pip install pre-commit
pip list
pip install pylint
pip list

# "Freeze" the requirements so we know what versions we are using.
pip freeze > requirements.txt && pip list
```

# Running the Program

You can run the program with

```
time python src/main.py
```

in your terminal after completing setup.
