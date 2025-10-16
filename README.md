# Assigment 5: Testing & CI in Financial Engineering

## Desgin notes

- The broker class is responsible for managing the cash and position of the portfolio.
- The engine class is responsible for running the backtest and executing the trades.
- The strategy class is responsible for generating the signals.
- The price loader class is responsible for loading the price data.
- The test suite is responsible for testing the broker, engine, and strategy classes.

## Coverage Report

![Coverage Report](cov.png)


Name                     Stmts   Miss  Cover
--------------------------------------------
backtester/__init__.py       0      0   100%
backtester/broker.py        21      0   100%
backtester/engine.py        23      1    96%
backtester/strategy.py      20      0   100%
tests/conftest.py           36      0   100%
tests/test_broker.py        68      0   100%
tests/test_engine.py        88      0   100%
tests/test_strategy.py      57      0   100%
--------------------------------------------
TOTAL                      313      1    99%

### Test Execution Commands

**Run all tests:**
```bash
PYTHONPATH=. pytest -q
coverage report
```
