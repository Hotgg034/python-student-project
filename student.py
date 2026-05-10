def get_grade(score):
    if score < 0 or score > 100:
        return "Error: Invalid score"
    if score >= 90:
        return "A"
    if score >= 75:
        return "B"
    if score >= 60:
        return "C"
    return "F"def get_grade(score):
    if score >= 90:
        return "A"
    return "B"
