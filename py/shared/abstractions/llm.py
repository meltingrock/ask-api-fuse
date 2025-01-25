"""Abstractions for the LLM model."""

import json
from enum import Enum
from typing import TYPE_CHECKING, Any, ClassVar, Optional

from openai.types.chat import ChatCompletion, ChatCompletionChunk
from pydantic import BaseModel, Field, ConfigDict

from .base import FUSESerializable

if TYPE_CHECKING:
    from .search import AggregateSearchResult

LLMChatCompletion = ChatCompletion
LLMChatCompletionChunk = ChatCompletionChunk


class RAGCompletion:
    completion: LLMChatCompletion
    search_results: "AggregateSearchResult"

    def __init__(
            self,
            completion: LLMChatCompletion,
            search_results: "AggregateSearchResult",
    ):
        self.completion = completion
        self.search_results = search_results


from typing import ClassVar, Optional, Dict, Any

from typing import Any, Dict, Optional, List
from pydantic import ConfigDict, Field, BaseModel
import json
from typing import ClassVar


class GenerationConfig(FUSESerializable):
    """Configuration for text generation."""

    # Class variable for defaults
    _defaults: ClassVar[Dict[str, Any]] = {
        "model": "openai/gpt-4o",
        "temperature": 0.1,
        "top_p": 1.0,
        "max_tokens_to_sample": 1024,
        "stream": False,
        "functions": None,
        "tools": None,
        "add_generation_kwargs": None,
        "api_base": None,
        "response_format": None,
    }

    # Pydantic V2 configuration
    model_config = ConfigDict(
        frozen=False,  # Explicitly make it non-frozen
        populate_by_name=True,
        json_encoders={},  # Add any custom encoders if needed
    )

    # Field definitions
    model: str = Field(
        default="openai/gpt-4o",
        description="The model to use for generation"
    )
    temperature: float = Field(
        default=0.1,
        description="Temperature for generation"
    )
    top_p: float = Field(
        default=1.0,
        description="Top p for generation"
    )
    max_tokens_to_sample: int = Field(
        default=1024,
        description="Maximum tokens to sample"
    )
    stream: bool = Field(
        default=False,
        description="Whether to stream the response"
    )
    functions: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Functions to use for generation"
    )
    tools: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Tools to use for generation"
    )
    add_generation_kwargs: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional generation kwargs"
    )
    api_base: Optional[str] = Field(
        default=None,
        description="API base URL"
    )
    response_format: Optional[Dict[str, Any] | BaseModel] = Field(
        default=None,
        description="Response format configuration"
    )

    @classmethod
    def set_default(cls, **kwargs):
        for key, value in kwargs.items():
            if key in cls._defaults:
                cls._defaults[key] = value
            else:
                raise AttributeError(
                    f"No default attribute '{key}' in GenerationConfig"
                )

    def __init__(self, **data):
        if (
                "response_format" in data
                and isinstance(data["response_format"], type)
                and issubclass(data["response_format"], BaseModel)
        ):
            model_class = data["response_format"]
            data["response_format"] = {
                "type": "json_schema",
                "json_schema": {
                    "name": model_class.__name__,
                    "schema": model_class.model_json_schema(),
                },
            }

        model = data.pop("model", None)
        if model is not None:
            super().__init__(model=model, **data)
        else:
            super().__init__(**data)

    def __str__(self):
        return json.dumps(self.to_dict())

    def __hash__(self):
        return hash((
            self.model,
            self.temperature,
            self.top_p,
            self.max_tokens_to_sample,
            self.stream,
            tuple(tuple(f.items()) for f in (self.functions or [])),
            tuple(tuple(t.items()) for t in (self.tools or [])),
            tuple(self.add_generation_kwargs.items()) if self.add_generation_kwargs else None,
            self.api_base,
            str(self.response_format) if self.response_format else None
        ))


class MessageType(Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    FUNCTION = "function"
    TOOL = "tool"

    def __str__(self):
        return self.value


class Message(FUSESerializable):
    role: MessageType | str
    content: Optional[str] = None
    name: Optional[str] = None
    function_call: Optional[dict[str, Any]] = None
    tool_calls: Optional[list[dict[str, Any]]] = None

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "role": "user",
            "content": "This is a test message.",
            "name": None,
            "function_call": None,
            "tool_calls": None,
        }
