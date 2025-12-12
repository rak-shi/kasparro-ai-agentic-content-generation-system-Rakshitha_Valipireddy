from pydantic import BaseModel
from typing import Any, Dict


class ParseProductInput(BaseModel):
    product: Dict[str, Any]


class GenerateQuestionsInput(BaseModel):
    product: Dict[str, Any]


class BuildFAQInput(BaseModel):
    product: Dict[str, Any]
    questions: Dict[str, Any]


class ProductOnlyInput(BaseModel):
    product: Dict[str, Any]
