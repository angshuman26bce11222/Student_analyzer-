def validate_score(score_str: str) -> float:
    """Validates and converts input string to a numerical score between 0 and 100."""
    try:
        score = float(score_str)
        if 0.0 <= score <= 100.0:
            return score
        raise ValueError("Score must be between 0 and 100.")
    except ValueError as e:
        print(f"[ValidationError] {e}")
        return -1.0