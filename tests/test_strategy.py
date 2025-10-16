import pandas as pd

def test_signals_length(strategy, prices):
    '''
    Test: signals length and type (shape/format)
    '''
    sig = strategy.signals(prices)
    assert len(sig) == len(prices)
    assert isinstance(sig, pd.Series)
    assert all(v in {-1, 0, 1} for v in sig)


def test_no_signals_on_insufficient_history(strategy, prices_short):
    '''
    Test: no signals when insufficient history
    '''
    sig = strategy.signals(prices_short)
    assert all(v == 0 for v in sig)

def test_buy_signals_on_price_jump(strategy_with_short_window, prices_with_jump):
    '''
    Test: buy signals on price jump
    '''
    sig = strategy_with_short_window.signals(prices_with_jump)
    # Expect buy signals after the jump (index > 150)
    assert any(sig[150:] == 1)
    # No sell signals in a rising market
    assert all(v != -1 for v in sig)