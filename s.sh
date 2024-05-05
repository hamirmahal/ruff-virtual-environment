echo && time ruff format --check
echo && time ruff check .
echo && time mypy --strict .
echo && python -m unittest src.utils.print_with_time
