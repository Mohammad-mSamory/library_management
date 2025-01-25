from dataclasses import dataclass, fields
from datetime import datetime
from typing import Any, Type, TypeVar, get_origin, get_args, Union
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
        kwargs = {}
        for field in fields(cls):
            value = data.get(field.name)
            
            # Handle field presence (even for falsy values)
            if field.name not in data:
                continue  
            
            # Extract type metadata
            field_type = field.type
            origin = get_origin(field_type)
            args = get_args(field_type)
            
            # Handle Optional[UUID], Union, etc.
            if origin is Union and type(None) in args:
                field_type = args[0]  
            
            # Convert based on type
            if field_type == UUID:
                kwargs[field.name] = UUID(value) if value else None
            elif field_type == datetime:
                kwargs[field.name] = datetime.fromisoformat(value)
            else:
                kwargs[field.name] = value
        
        return cls(**kwargs) 