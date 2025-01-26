from dataclasses import dataclass, fields
from datetime import datetime
from typing import Any, Type, TypeVar, Union, get_args, get_origin
from uuid import UUID

T = TypeVar('T', bound='BaseEntity')


@dataclass
class BaseEntity:
    def to_dict(self) -> dict:
        result = {}
        for field in fields(self):
            value = getattr(self, field.name)
            if isinstance(value, UUID):
                result[field.name] = str(value)
            elif isinstance(value, datetime):
                result[field.name] = value.isoformat()
            else:
                result[field.name] = value
        return result

    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        kwargs: dict[str, Any] = {}
        for field in fields(cls):
            if field.name not in data:
                continue

            value = data.get(field.name)

            # Handle None values
            if value is None:
                # ... (existing null handling code remains) ...
                continue

            # Get field type (handling Optional)
            field_type = field.type
            field_origin = get_origin(field_type)
            field_args = get_args(field_type)

            if field_origin is Union:
                non_none_types = [t for t in field_args if t is not type(None)]
                if len(non_none_types) == 1:
                    field_type = non_none_types[0]

            # Type conversions
            if field_type == UUID:
                if isinstance(value, str):
                    kwargs[field.name] = UUID(value)
                elif isinstance(value, UUID):
                    kwargs[field.name] = value
                else:
                    raise ValueError(f"Invalid UUID value: {value}")
            elif field_type == datetime:
                if isinstance(value, str):
                    kwargs[field.name] = datetime.fromisoformat(value)
                elif isinstance(value, datetime):
                    kwargs[field.name] = value
                else:
                    raise ValueError(f"Invalid datetime value: {value}")
            else:
                kwargs[field.name] = value

        return cls(**kwargs)
