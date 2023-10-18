def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    students = 0

    for start, end in permanence_period:
        if not (isinstance(start, int) and isinstance(end, int)):
            return None
        if start <= target_time <= end:
            students += 1
    return students
