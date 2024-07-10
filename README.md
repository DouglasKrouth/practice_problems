# practice_problems

## To Run
1. Install `Python 3.12` and `poetry` [[link](https://python-poetry.org/docs/)]
2. `git clone` the repo to desired directory, `cd` into it
3. Call `poetry install` to fetch dependencies (only `pytest` used as of 07102024)
4. Call `poetry run pytest`, review output

## Test Output
```
==================================================================== test session starts =====================================================================
platform linux -- Python 3.12.4, pytest-8.2.2, pluggy-1.5.0 -- /home/dk/Development/practice_problems/.venv/bin/python
cachedir: .pytest_cache
rootdir: /home/dk/Development/practice_problems
configfile: pyproject.toml
testpaths: tests
collected 1 item                                                                                                                                             

tests/test_problem_one.py::test_get_best_group_prices PASSED                                                                                           [100%]

===================================================================== 1 passed in 0.02s ======================================================================
```
