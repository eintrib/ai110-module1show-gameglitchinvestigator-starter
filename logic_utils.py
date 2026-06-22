def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


# I worked with Claude (an AI assistant) to fix the high/low hint bug in this
# function. The original code in app.py turned the secret into a string on even
# attempts, which made it compare guesses alphabetically instead of numerically
# (e.g. "9" > "100"), so the game told me to go HIGHER when it should have said
# LOWER. The "Too High"/"Too Low" messages were also reversed. Claude walked me
# through the cause step by step, then I had it move this function here, drop the
# string-comparison path, and fix the messages. We also added regression tests.
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go LOWER!"
    return "Too Low", "📉 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
