import logging
import textwrap
from typing import Optional

from fastapi import Body, Depends, Path, Query

from core.base import FUSEException
from core.base.api.models import (
    GenericBooleanResponse,
    GenericMessageResponse,
    WrappedBooleanResponse,
    WrappedGenericMessageResponse,
    WrappedPromptResponse,
    WrappedPromptsResponse,
)

from ...abstractions import FUSEProviders, FUSEServices
from .base_router import BaseRouterV3


class PromptsRouter(BaseRouterV3):
    def __init__(
        self,
        providers: FUSEProviders,
        services: FUSEServices,
    ):
        logging.info("Initializing PromptsRouter")
        super().__init__(providers, services)

    def _setup_routes(self):
        @self.router.post(
            "",
            dependencies=[Depends(self.rate_limit_dependency)],
            summary="Create a new prompt",
        )
        @self.base_endpoint
        async def create_prompt(
            name: str = Body(..., description="The name of the prompt"),
            template: str = Body(
                ..., description="The template string for the prompt"
            ),
            input_types: dict[str, str] = Body(
                default={},
                description="A dictionary mapping input names to their types",
            ),
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedGenericMessageResponse:
            """
            Create a new prompt with the given configuration.

            This endpoint allows superusers to create a new prompt with a specified name, template, and input types.
            """
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can create prompts.",
                    403,
                )
            result = await self.services.management.add_prompt(
                name, template, input_types
            )
            return GenericMessageResponse(message=result)  # type: ignore

        @self.router.get(
            "",
            dependencies=[Depends(self.rate_limit_dependency)],
            summary="List all prompts",
        )
        @self.base_endpoint
        async def get_prompts(
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedPromptsResponse:
            """
            List all available prompts.

            This endpoint retrieves a list of all prompts in the system. Only superusers can access this endpoint.
            """
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can list prompts.",
                    403,
                )
            get_prompts_response = (
                await self.services.management.get_all_prompts()
            )

            return (  # type: ignore
                get_prompts_response["results"],
                {
                    "total_entries": get_prompts_response["total_entries"],
                },
            )

        @self.router.post(
            "/{name}",
            dependencies=[Depends(self.rate_limit_dependency)],
            summary="Get a specific prompt",
        )
        @self.base_endpoint
        async def get_prompt(
            name: str = Path(..., description="Prompt name"),
            inputs: Optional[dict[str, str]] = Body(
                None, description="Prompt inputs"
            ),
            prompt_override: Optional[str] = Query(
                None, description="Prompt override"
            ),
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedPromptResponse:
            """
            Get a specific prompt by name, optionally with inputs and override.

            This endpoint retrieves a specific prompt and allows for optional inputs and template override.
            Only superusers can access this endpoint.
            """
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can retrieve prompts.",
                    403,
                )
            result = await self.services.management.get_prompt(
                name, inputs, prompt_override
            )
            return result  # type: ignore

        @self.router.put(
            "/{name}",
            dependencies=[Depends(self.rate_limit_dependency)],
            summary="Update an existing prompt",
        )
        @self.base_endpoint
        async def update_prompt(
            name: str = Path(..., description="Prompt name"),
            template: Optional[str] = Body(
                None, description="Updated prompt template"
            ),
            input_types: dict[str, str] = Body(
                default={},
                description="A dictionary mapping input names to their types",
            ),
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedGenericMessageResponse:
            """
            Update an existing prompt's template and/or input types.

            This endpoint allows superusers to update the template and input types of an existing prompt.
            """
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can update prompts.",
                    403,
                )
            result = await self.services.management.update_prompt(
                name, template, input_types
            )
            return GenericMessageResponse(message=result)  # type: ignore

        @self.router.delete(
            "/{name}",
            dependencies=[Depends(self.rate_limit_dependency)],
            summary="Delete a prompt",
        )
        @self.base_endpoint
        async def delete_prompt(
            name: str = Path(..., description="Prompt name"),
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedBooleanResponse:
            """
            Delete a prompt by name.

            This endpoint allows superusers to delete an existing prompt.
            """
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can delete prompts.",
                    403,
                )
            await self.services.management.delete_prompt(name)
            return GenericBooleanResponse(success=True)  # type: ignore
