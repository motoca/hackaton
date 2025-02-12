# pydantic_compat.py
import pydantic

if pydantic.__version__.startswith('2'):
    from pydantic import v1 as pydantic
    BaseModel = pydantic.BaseModel
    Field = pydantic.Field
else:
    from pydantic import BaseModel, Field