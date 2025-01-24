from dataclasses import dataclass
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel

from core.providers import (
    AsyncSMTPEmailProvider,
    ConsoleMockEmailProvider,
    HatchetOrchestrationProvider,
    JwtAuthProvider,
    LiteLLMCompletionProvider,
    LiteLLMEmbeddingProvider,
    OllamaEmbeddingProvider,
    OpenAICompletionProvider,
    OpenAIEmbeddingProvider,
    PostgresDatabaseProvider,
    FUSEAuthProvider,
    FUSEIngestionProvider,
    SendGridEmailProvider,
    SimpleOrchestrationProvider,
    SupabaseAuthProvider,
    UnstructuredIngestionProvider,
)

if TYPE_CHECKING:
    from core.main.services.auth_service import AuthService
    from core.main.services.graph_service import GraphService
    from core.main.services.ingestion_service import IngestionService
    from core.main.services.management_service import ManagementService
    from core.main.services.retrieval_service import RetrievalService


class FUSEProviders(BaseModel):
    auth: FUSEAuthProvider | SupabaseAuthProvider | JwtAuthProvider
    database: PostgresDatabaseProvider
    ingestion: FUSEIngestionProvider | UnstructuredIngestionProvider
    embedding: (
        LiteLLMEmbeddingProvider
        | OpenAIEmbeddingProvider
        | OllamaEmbeddingProvider
    )
    llm: LiteLLMCompletionProvider | OpenAICompletionProvider
    orchestration: HatchetOrchestrationProvider | SimpleOrchestrationProvider
    email: (
        AsyncSMTPEmailProvider
        | ConsoleMockEmailProvider
        | SendGridEmailProvider
    )

    class Config:
        arbitrary_types_allowed = True


@dataclass
class FUSEServices:
    auth: "AuthService"
    ingestion: "IngestionService"
    management: "ManagementService"
    retrieval: "RetrievalService"
    graph: "GraphService"
