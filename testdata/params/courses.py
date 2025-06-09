from dataclasses import dataclass
from typing import Optional


@dataclass
class CourseCardParams:
    index: Optional[int] = 0
    title: str = ""
    estimated_time: str = ""
    description: str = ""
    max_score: str = "0"
    min_score: str = "0"
