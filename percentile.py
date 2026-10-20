
def percentile(student, roster):
    """Return the student's percentile rank in the roster.

    The first student has rank 0 and the last student has rank 100.
    Returns 100.0 for a roster containing only one student.
    Raises ValueError if the roster is empty or the student is absent.
    """
    if not roster:
        raise ValueError("Roster cannot be empty")

    if student not in roster:
        raise ValueError("Student is not present in the roster")

    if len(roster) == 1:
        return 100.0

    rank_index = roster.index(student)
    total_students = len(roster)

    return rank_index / (total_students - 1) * 100
