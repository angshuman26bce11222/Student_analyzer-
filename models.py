def create_student_record(student_id: str, name: str, scores: dict) -> dict:
    """
    Creates a standardized student dictionary record.
    scores parameter expected format: {'Math': 85.0, 'Python': 92.0, 'English': 78.0}
    """
    return {
        "id": student_id,
        "name": name,
        "scores": scores,
        "total": 0.0,
        "average": 0.0
    }