import logging

# Keep '*' imports for enhanced development velocity
from .agent import *
from .base import *
from .main import *
from .parsers import *
from .providers import *

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a console handler and set the level to info
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create a formatter and set it for the handler
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)
ch.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(ch)

# Optional: Prevent propagation to the root logger
logger.propagate = False

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("LiteLLM").setLevel(logging.WARNING)


__all__ = [
    "FUSEAgent",
    "FUSEStreamingAgent",
    "FUSERAGAgent",
    "FUSEStreamingRAGAgent",
    "AsyncSyncMeta",
    "syncable",
    "MessageType",
    "Document",
    "DocumentChunk",
    "DocumentResponse",
    "IngestionStatus",
    "KGExtractionStatus",
    "KGEnrichmentStatus",
    "DocumentType",
    "EmbeddingPurpose",
    "default_embedding_prefixes",
    "FUSEDocumentProcessingError",
    "FUSEException",
    "Entity",
    "KGExtraction",
    "Relationship",
    "GenerationConfig",
    "LLMChatCompletion",
    "LLMChatCompletionChunk",
    "RAGCompletion",
    "Prompt",
    "AggregateSearchResult",
    "WebSearchResponse",
    "GraphSearchResult",
    "ChunkSearchSettings",
    "GraphSearchSettings",
    "ChunkSearchResult",
    "SearchSettings",
    "select_search_filters",
    "SearchMode",
    "HybridSearchSettings",
    "Token",
    "TokenData",
    "Vector",
    "VectorEntry",
    "VectorType",
    "IndexConfig",
    "Agent",
    "AgentConfig",
    "Conversation",
    "Message",
    "Tool",
    "ToolResult",
    "TokenResponse",
    "User",
    "AppConfig",
    "Provider",
    "ProviderConfig",
    "AuthConfig",
    "AuthProvider",
    "CryptoConfig",
    "CryptoProvider",
    "EmailConfig",
    "EmailProvider",
    "LimitSettings",
    "DatabaseConfig",
    "DatabaseProvider",
    "EmbeddingConfig",
    "EmbeddingProvider",
    "CompletionConfig",
    "CompletionProvider",
    "RecursiveCharacterTextSplitter",
    "TextSplitter",
    "to_async_generator",
    "generate_id",
    "increment_version",
    "validate_uuid",
    "FUSEProviders",
    "FUSEApp",
    "FUSEBuilder",
    "FUSEConfig",
    "FUSEProviderFactory",
    "AuthService",
    "IngestionService",
    "ManagementService",
    "RetrievalService",
    "GraphService",
    "AudioParser",
    "BMPParser",
    "DOCParser",
    "DOCXParser",
    "ImageParser",
    "ODTParser",
    "VLMPDFParser",
    "BasicPDFParser",
    "PDFParserUnstructured",
    "PPTParser",
    "PPTXParser",
    "RTFParser",
    "CSVParser",
    "CSVParserAdvanced",
    "EMLParser",
    "EPUBParser",
    "JSONParser",
    "MSGParser",
    "ORGParser",
    "P7SParser",
    "RSTParser",
    "TIFFParser",
    "TSVParser",
    "XLSParser",
    "XLSXParser",
    "XLSXParserAdvanced",
    "MDParser",
    "HTMLParser",
    "TextParser",
    "SupabaseAuthProvider",
    "FUSEAuthProvider",
    "JwtAuthProvider",
    # Email
    # Crypto
    "BCryptCryptoProvider",
    "BcryptCryptoConfig",
    "NaClCryptoConfig",
    "NaClCryptoProvider",
    "PostgresDatabaseProvider",
    "LiteLLMEmbeddingProvider",
    "OpenAIEmbeddingProvider",
    "OllamaEmbeddingProvider",
    "OpenAICompletionProvider",
    "LiteLLMCompletionProvider",
    "UnstructuredIngestionProvider",
    "FUSEIngestionProvider",
    "ChunkingStrategy",
]
