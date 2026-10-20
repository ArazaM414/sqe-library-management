def percentile(student, roster):
    rank_index = roster.index(student)
    total_students = len(roster)
    return rank_index / total_students * 100