import logging
import textwrap
from datetime import datetime, timezone

import psutil
from fastapi import Depends

from core.base import FUSEException
from core.base.api.models import (
    GenericMessageResponse,
    WrappedGenericMessageResponse,
    WrappedServerStatsResponse,
    WrappedSettingsResponse,
)

from ...abstractions import FUSEProviders, FUSEServices
from .base_router import BaseRouterV3


class SystemRouter(BaseRouterV3):
    def __init__(
        self,
        providers: FUSEProviders,
        services: FUSEServices,
    ):
        logging.info("Initializing SystemRouter")
        super().__init__(providers, services)
        self.start_time = datetime.now(timezone.utc)

    def _setup_routes(self):
        @self.router.get(
            "/health",
            # dependencies=[Depends(self.rate_limit_dependency)],
        )
        @self.base_endpoint
        async def health_check() -> WrappedGenericMessageResponse:
            return GenericMessageResponse(message="ok")  # type: ignore

        @self.router.get(
            "/system/settings",
            dependencies=[Depends(self.rate_limit_dependency)],
        )
        @self.base_endpoint
        async def app_settings(
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedSettingsResponse:
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only a superuser can call the `system/settings` endpoint.",
                    403,
                )
            return await self.services.management.app_settings()

        @self.router.get(
            "/system/status",
            dependencies=[Depends(self.rate_limit_dependency)],
        )
        @self.base_endpoint
        async def server_stats(
            auth_user=Depends(self.providers.auth.auth_wrapper()),
        ) -> WrappedServerStatsResponse:
            if not auth_user.is_superuser:
                raise FUSEException(
                    "Only an authorized user can call the `system/status` endpoint.",
                    403,
                )
            return {  # type: ignore
                "start_time": self.start_time.isoformat(),
                "uptime_seconds": (
                    datetime.now(timezone.utc) - self.start_time
                ).total_seconds(),
                "cpu_usage": psutil.cpu_percent(),
                "memory_usage": psutil.virtual_memory().percent,
            }
