from dataclasses import dataclass, field
# from datetime import datetime
# from typing import List, Optional


@dataclass
class ThreadDomain():
    id: int
    title: str
    week_id: int

@dataclass
class CreateThreadSpec:
    week_id: int
    title: str

