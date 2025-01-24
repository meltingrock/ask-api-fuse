import logging
from typing import Any, Type

from ..abstractions import FUSEProviders, FUSEServices
from ..api.v3.chunks_router import ChunksRouter
from ..api.v3.collections_router import CollectionsRouter
from ..api.v3.conversations_router import ConversationsRouter
from ..api.v3.documents_router import DocumentsRouter
from ..api.v3.graph_router import GraphRouter
from ..api.v3.indices_router import IndicesRouter
from ..api.v3.logs_router import LogsRouter
from ..api.v3.prompts_router import PromptsRouter
from ..api.v3.retrieval_router import RetrievalRouterV3
from ..api.v3.system_router import SystemRouter
from ..api.v3.users_router import UsersRouter
from ..app import FUSEApp
from ..config import FUSEConfig
from ..services.auth_service import AuthService
from ..services.graph_service import GraphService
from ..services.ingestion_service import IngestionService
from ..services.management_service import ManagementService
from ..services.retrieval_service import RetrievalService
from .factory import FUSEProviderFactory

logger = logging.getLogger()


class FUSEBuilder:
    _SERVICES = ["auth", "ingestion", "management", "retrieval", "graph"]

    def __init__(self, config: FUSEConfig):
        self.config = config

    async def _create_providers(
        self, provider_factory: Type[FUSEProviderFactory], *args, **kwargs
    ) -> Any:
        factory = provider_factory(self.config)
        return await factory.create_providers(*args, **kwargs)

    async def build(self, *args, **kwargs) -> FUSEApp:
        provider_factory = FUSEProviderFactory

        try:
            providers = await self._create_providers(
                provider_factory, *args, **kwargs
            )
        except Exception as e:
            logger.error(f"Error {e} while creating FUSEProviders.")
            raise

        service_params = {
            "config": self.config,
            "providers": providers,
        }

        services = self._create_services(service_params)

        routers = {
            "chunks_router": ChunksRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "collections_router": CollectionsRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "conversations_router": ConversationsRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "documents_router": DocumentsRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "graph_router": GraphRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "indices_router": IndicesRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "logs_router": LogsRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "prompts_router": PromptsRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "retrieval_router_v3": RetrievalRouterV3(
                providers=providers,
                services=services,
            ).get_router(),
            "system_router": SystemRouter(
                providers=providers,
                services=services,
            ).get_router(),
            "users_router": UsersRouter(
                providers=providers,
                services=services,
            ).get_router(),
        }

        return FUSEApp(
            config=self.config,
            orchestration_provider=providers.orchestration,
            services=services,
            **routers,
        )

    async def _create_providers(
        self, provider_factory: Type[FUSEProviderFactory], *args, **kwargs
    ) -> FUSEProviders:
        factory = provider_factory(self.config)
        return await factory.create_providers(*args, **kwargs)

    def _create_services(self, service_params: dict[str, Any]) -> FUSEServices:
        services = FUSEBuilder._SERVICES
        service_instances = {}

        for service_type in services:
            service_class = globals()[f"{service_type.capitalize()}Service"]
            service_instances[service_type] = service_class(**service_params)

        return FUSEServices(**service_instances)
