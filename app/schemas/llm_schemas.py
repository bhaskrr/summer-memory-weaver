from pydantic import BaseModel
from typing import List

class ThemeResponseSchema(BaseModel):
    themes: List[str]