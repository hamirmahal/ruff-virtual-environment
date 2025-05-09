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
pip install -r requirements.txt
```

## To install the `pre-commit` hooks

```
pre-commit install
```

## To install the latest packages

```
pip install ruff
pip install pylint
pip install pyright
pip install pre-commit

pip freeze >requirements.txt # Lock dependency versions.
```

# To Run the Program

You can run the program with

```
python src/main.py
```

in your terminal after completing setup.
