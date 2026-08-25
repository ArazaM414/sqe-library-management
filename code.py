class Student:
    """Student record aur unke marks store karne ke liye class."""

    def __init__(self, name: str, roll_no: str, scores: list[float] | None = None):
        self.name = name
        self.roll_no = roll_no
        self.scores = scores if scores is not None else []

    def add_score(self, score: float):
        """Negative marks reject karta hai."""
        if score < 0:
            raise ValueError("Score negative nahi ho sakta!")
        self.scores.append(score)
        
        def calculate_fine(days_overdue: int, daily_rate: float) -> float:
    if days_overdue < 0 or daily_rate < 0:
        raise ValueError("Overdue days aur daily rate negative nahi ho sakte!")
    return days_overdue * daily_rate

    def average(self) -> float:
        """Average calculate karta hai. Agar score list khali ho toh 0.0 return karega."""
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)