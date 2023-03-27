import uuid
from datetime import datetime
from typing import Optional
import pytz

from pydantic import BaseModel, Field, root_validator


class Pod(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    name: str = Field(...)
    garden_id: str = Field(...)
    location: list[int] = Field(...)  # [row, column]
    plant: str = None
    created_at: datetime = datetime.now(pytz.timezone("US/Eastern"))
    updated_at: datetime = datetime.now(pytz.timezone("US/Eastern"))

    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "66608a32-a24c-4b70-ae2c-c46c586ea0c3",
                "name": "John's Lettuce",
                "garden_id": "77608a32-a45c-4b70-ae2c-c46c586ea0c3",
                "location": "[1, 3]",
                "created_at": "2023-02-17T20:19:00.536083",
                "updated_at": "2023-02-17T20:19:00.536084",
            }
        }

        @root_validator
        def number_validator(cls, values):
            values["updated_at"] = datetime.now(pytz.timezone("US/Eastern"))
            return values


class PodUpdate(BaseModel):
    name: Optional[str]
    garden_id: Optional[str]
    location: Optional[list[int]]
    plant: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "name": "Jack's Lettuce",
                "garden_id": "77608a32-a45c-4b70-ae2c-c46c586ea0c3",
                "location": "[2, 6]",
                "plant": "Lettuce",
            }
        }
