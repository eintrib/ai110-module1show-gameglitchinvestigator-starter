from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_single_digit_guess_below_multi_digit_secret():
    # Regression test for the high/low bug.
    #
    # Old bug: on even attempts the secret was passed as a STRING, so
    # check_guess compared lexicographically. "9" > "100" is True, so a
    # guess of 9 against secret 100 was wrongly reported as "Too High"
    # (telling the player to go LOWER) when 9 is numerically too LOW.
    #
    # The fix compares numerically, so 9 vs 100 must be "Too Low".
    outcome, message = check_guess(9, 100)
    assert outcome == "Too Low"
    assert message == "📉 Go HIGHER!"


def test_too_high_tells_player_to_go_lower():
    # The fixed messages must point the right direction:
    # a guess that is too high should tell the player to go LOWER.
    outcome, message = check_guess(100, 9)
    assert outcome == "Too High"
    assert message == "📈 Go LOWER!"
