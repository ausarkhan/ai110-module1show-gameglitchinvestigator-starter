from logic_utils import check_guess, get_range_for_difficulty, parse_guess


def test_check_guess_too_high():
    outcome, msg = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in msg


def test_check_guess_too_low():
    outcome, msg = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in msg


def test_check_guess_win():
    outcome, msg = check_guess(50, 50)
    assert outcome == "Win"


def test_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_blank():
    ok, val, err = parse_guess("")
    assert ok is False
    assert val is None
    assert err is not None


def test_parse_guess_float_string():
    ok, val, err = parse_guess("12.0")
    assert ok is True
    assert val == 12
    assert err is None