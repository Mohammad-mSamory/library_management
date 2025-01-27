from dataclasses import dataclass, fields
from datetime import date, datetime
from enum import Enum
from typing import Any, Type, TypeVar
from uuid import UUID

T = TypeVar('T', bound='BaseEntity')


def get_field_value(
    field_type: type[Any] | str | Any, field_data: Any
) -> Any:
    if field_data is None:
        return None
    if isinstance(field_type, type) and issubclass(field_type, BaseEntity):
        return field_type.from_dict(field_data)

    origin = getattr(field_type, "__origin__", None)
    if origin is list and isinstance(field_data, list):
        args = getattr(field_type, "__args__", [])
        if args and isinstance(args[0], type) and issubclass(
                args[0], BaseEntity):
            return [args[0].from_dict(item) for item in field_data]

    return field_data


def get_attr_value(
    attr_val: Any, map_primitive: bool = True
) -> Any:
    if attr_val is None:
        return None

    if isinstance(attr_val, BaseEntity):
        return attr_val.to_dict()

    if isinstance(attr_val, list):
        return [get_attr_value(item) for item in attr_val]

    if not map_primitive:
        return attr_val

    if isinstance(attr_val, UUID):
        return str(attr_val)

    if isinstance(attr_val, datetime):
        return attr_val.isoformat()

    if isinstance(attr_val, date):
        return attr_val.isoformat()

    if isinstance(attr_val, Enum):
        return attr_val.value

    return attr_val


@dataclass
class BaseEntity:
    created_by: UUID
    created_at: datetime
    updated_by: UUID
    updated_at: datetime

    @classmethod
    def from_dict(
        cls: Type[T], data: dict[str, Any], exclude: list[str] | None = None
    ) -> T:
        """
        Convert a dictionary to an instance of the class.
        Recursively handles nested data classes and lists of data classes.
        """
        # If 'exclude' is provided, use it directly instead of relying on
        # config
        excluded_fields = exclude if exclude else []

        instance_data = {}
        entity_fields = {f.name: f.type for f in fields(cls)}
        for field_name, field_type in entity_fields.items():
            field_data = None
            if field_name not in excluded_fields:
                field_data = data.get(field_name, None)
            instance_data[field_name] = get_field_value(field_type, field_data)

        return cls(**instance_data)

    def to_dict(
        self, exclude: list[str] | None = None, map_primitive: bool = True
    ) -> dict[str, Any]:
        """
        Convert the current object to a dictionary and handle nested
        dataclasses.
        Recursively converts all nested dataclasses to dictionaries.
        """
        # If 'exclude' is provided, use it directly instead of relying on
        # config
        excluded_fields = exclude if exclude else []

        data: dict[str, Any] = {}
        for cls in self.__class__.mro():
            if not hasattr(cls, '__annotations__'):
                continue
            entity_fields = [f.name for f in fields(cls)]
            for field_name in entity_fields:
                if field_name not in excluded_fields:
                    data[field_name] = get_attr_value(
                        getattr(self, field_name, None), map_primitive
                    )

        return data
