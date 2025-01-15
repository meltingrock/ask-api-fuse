py/core/main/orchestration/hatchet/ingestion_workflow.py:from core.base.abstractions import DocumentResponse, FUSEException
py/core/main/orchestration/hatchet/ingestion_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/ingestion_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/ingestion_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/ingestion_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/kg_workflow.py:from core.base import OrchestrationProvider, FUSEException
py/core/main/orchestration/hatchet/kg_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/kg_workflow.py:                raise FUSEException(
py/core/main/orchestration/hatchet/kg_workflow.py:                    raise FUSEException("No communities found", 400)
py/core/main/orchestration/simple/ingestion_workflow.py:    FUSEException,
py/core/main/orchestration/simple/ingestion_workflow.py:                            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/ingestion_workflow.py:                        raise FUSEException(
py/core/main/orchestration/simple/kg_workflow.py:from core import GenerationConfig, FUSEException
py/core/main/orchestration/simple/kg_workflow.py:            raise FUSEException(
py/core/main/orchestration/simple/kg_workflow.py:                raise FUSEException("No communities found", 400)
py/core/main/app.py:from core.base import FUSEException
py/core/main/app.py:        @self.app.exception_handler(FUSEException)
py/core/main/app.py:        async def fuse_exception_handler(request: Request, exc: FUSEException):
py/core/main/app_entry.py:from core.base import FUSEException
py/core/main/app_entry.py:@app.exception_handler(FUSEException)
py/core/main/app_entry.py:async def fuse_exception_handler(request: Request, exc: FUSEException):
py/core/main/services/ingestion_service.py:    FUSEException,
py/core/main/services/ingestion_service.py:                raise FUSEException(
py/core/main/services/ingestion_service.py:                raise FUSEException(
py/core/main/services/ingestion_service.py:                    raise FUSEException(
py/core/main/services/ingestion_service.py:                    raise FUSEException(
py/core/main/services/ingestion_service.py:        except FUSEException as e:
py/core/main/services/ingestion_service.py:            logger.error(f"FUSEException in ingest_file_ingress: {str(e)}")
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/ingestion_service.py:                raise FUSEException(
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/ingestion_service.py:            raise FUSEException(
py/core/main/services/management_service.py:    FUSEException,
py/core/main/services/management_service.py:                raise FUSEException(
py/core/main/services/management_service.py:                raise FUSEException(
py/core/main/services/management_service.py:            raise FUSEException(status_code=400, message=str(e))
py/core/main/services/management_service.py:            raise FUSEException(status_code=404, message=str(e))
py/core/main/services/management_service.py:            raise FUSEException(status_code=404, message=str(e))
py/core/main/services/management_service.py:            raise FUSEException(status_code=404, message=str(e))
py/core/main/services/management_service.py:            raise FUSEException(status_code=404, message=str(e))
py/core/main/services/auth_service.py:from core.base import FUSEException, RunManager, Token
py/core/main/services/auth_service.py:            raise FUSEException(
py/core/main/services/auth_service.py:            raise FUSEException(
py/core/main/services/auth_service.py:            raise FUSEException(
py/core/main/services/auth_service.py:            raise FUSEException(
py/core/main/services/auth_service.py:            raise FUSEException(status_code=404, message="User not found")
py/core/main/services/auth_service.py:            raise FUSEException(status_code=404, message="User not found")
py/core/main/services/auth_service.py:            raise FUSEException(status_code=404, message="User not found")
py/core/main/services/auth_service.py:            raise FUSEException(
py/core/main/services/auth_service.py:            raise FUSEException(status_code=400, message="Incorrect password")
py/core/main/services/retrieval_service.py:    FUSEException,
py/core/main/services/retrieval_service.py:                raise FUSEException(
py/core/main/services/retrieval_service.py:                raise FUSEException(
py/core/main/services/retrieval_service.py:                    raise FUSEException(
py/core/main/services/retrieval_service.py:                    raise FUSEException(
py/core/main/services/retrieval_service.py:                    raise FUSEException(
py/core/main/services/retrieval_service.py:                        raise FUSEException(
py/core/main/services/retrieval_service.py:                    raise FUSEException(
py/core/main/services/graph_service.py:    FUSEException,
py/core/main/services/graph_service.py:            raise FUSEException(
py/core/main/services/graph_service.py:                    raise FUSEException(
py/core/main/services/graph_service.py:                        raise FUSEException(
py/core/main/services/graph_service.py:                        raise FUSEException(
py/core/main/services/graph_service.py:                        raise FUSEException(
py/core/main/services/graph_service.py:                FUSEException,
py/core/main/api/v3/users_router.py:from core.base import FUSEException
py/core/main/api/v3/users_router.py:            #     raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/users_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:    FUSEException,
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                    raise FUSEException("Empty list of chunks provided", 400)
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                        raise FUSEException(
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                        raise FUSEException(
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                    raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException(status_code=404, message="File not found.")
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:            #     raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/documents_router.py:            #     raise FUSEException(
py/core/main/api/v3/documents_router.py:                raise FUSEException("Document not found.", 404)
py/core/main/api/v3/documents_router.py:                raise FUSEException(
py/core/main/api/v3/retrieval_router.py:    FUSEException,
py/core/main/api/v3/retrieval_router.py:                raise FUSEException("Query cannot be empty", 400)
py/core/main/api/v3/retrieval_router.py:                raise FUSEException(str(e), 500)
py/core/main/api/v3/prompts_router.py:from core.base import FUSEException
py/core/main/api/v3/prompts_router.py:                raise FUSEException(
py/core/main/api/v3/prompts_router.py:                raise FUSEException(
py/core/main/api/v3/prompts_router.py:                raise FUSEException(
py/core/main/api/v3/prompts_router.py:                raise FUSEException(
py/core/main/api/v3/prompts_router.py:                raise FUSEException(
py/core/main/api/v3/indices_router.py:from core.base import IndexConfig, FUSEException
py/core/main/api/v3/indices_router.py:                raise FUSEException(
py/core/main/api/v3/chunks_router.py:    FUSEException,
py/core/main/api/v3/chunks_router.py:                raise FUSEException("Chunk not found", 404)
py/core/main/api/v3/chunks_router.py:                raise FUSEException("Not authorized to access this chunk", 403)
py/core/main/api/v3/chunks_router.py:                raise FUSEException(f"Chunk {chunk_update.id} not found", 404)
py/core/main/api/v3/chunks_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:from core.base import KGEnrichmentStatus, FUSEException, Workflow
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Collection not found.", 404)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Only superusers can reset a graph", 403)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Entity not found", 404)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Relationship not found", 404)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Community not found", 404)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Collection not found.", 404)
py/core/main/api/v3/graph_router.py:                raise FUSEException("Only superusers can `pull` a graph.", 403)
py/core/main/api/v3/graph_router.py:                raise FUSEException(
py/core/main/api/v3/graph_router.py:                raise FUSEException("Graph not found", 404)
py/core/main/api/v3/system_router.py:from core.base import FUSEException
py/core/main/api/v3/system_router.py:                raise FUSEException(
py/core/main/api/v3/system_router.py:                raise FUSEException(
py/core/main/api/v3/conversations_router.py:from core.base import Message, FUSEException
py/core/main/api/v3/conversations_router.py:                raise FUSEException(
py/core/main/api/v3/conversations_router.py:                raise FUSEException(
py/core/main/api/v3/conversations_router.py:                raise FUSEException("Content cannot be empty", status_code=400)
py/core/main/api/v3/conversations_router.py:                raise FUSEException("Invalid role", status_code=400)
py/core/main/api/v3/base_router.py:from core.base import FUSEException, manage_run
py/core/main/api/v3/base_router.py:                except FUSEException:
py/core/main/api/v3/collections_router.py:from core.base import KGCreationSettings, KGRunType, FUSEException
py/core/main/api/v3/collections_router.py:from core.base import FUSEException
py/core/main/api/v3/collections_router.py:        raise FUSEException("The specified collection does not exist.", 404)
py/core/main/api/v3/collections_router.py:            raise FUSEException(
py/core/main/api/v3/collections_router.py:    raise FUSEException("You do not have access to this collection.", 403)
py/core/main/api/v3/collections_router.py:                raise FUSEException(
py/core/main/api/v3/collections_router.py:                raise FUSEException(
py/core/main/api/v3/collections_router.py:                raise FUSEException(
py/core/main/api/v3/collections_router.py:                raise FUSEException(
py/core/providers/embeddings/litellm.py:    FUSEException,
py/core/providers/embeddings/litellm.py:            raise FUSEException(error_msg, 400)
py/core/providers/embeddings/litellm.py:            raise FUSEException(error_msg, 400)
py/core/providers/embeddings/ollama.py:    FUSEException,
py/core/providers/embeddings/ollama.py:            raise FUSEException(error_msg, 400)
py/core/providers/embeddings/ollama.py:            raise FUSEException(error_msg, 400)
py/core/providers/auth/supabase.py:    FUSEException,
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(status_code=401, message="Invalid token")
py/core/providers/auth/supabase.py:            raise FUSEException(status_code=400, message="Inactive user")
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/supabase.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:    FUSEException,
py/core/providers/auth/fuse_auth.py:        except FUSEException:
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=401, message="Invalid token claims")
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=401, message="Token has expired")
py/core/providers/auth/fuse_auth.py:        Returns a User if successful, or raises FUSEException if not.
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=401, message="Invalid API key")
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=401, message="Invalid API key")
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:                raise FUSEException(
py/core/providers/auth/fuse_auth.py:                raise FUSEException(
py/core/providers/auth/fuse_auth.py:        except FUSEException:
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=400, message="Inactive user")
py/core/providers/auth/fuse_auth.py:                raise FUSEException(
py/core/providers/auth/fuse_auth.py:                raise FUSEException(
py/core/providers/auth/fuse_auth.py:                raise FUSEException(
py/core/providers/auth/fuse_auth.py:                raise FUSEException(status_code=404, message="User not found")
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(status_code=401, message="Email not verified")
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:        except FUSEException as e:
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:                        raise FUSEException(
py/core/providers/auth/fuse_auth.py:                        raise FUSEException(
py/core/providers/auth/fuse_auth.py:        except FUSEException:
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/providers/auth/fuse_auth.py:            raise FUSEException(
py/core/database/graphs.py:    FUSEException,
py/core/database/graphs.py:            raise FUSEException(status_code=400, message="No fields to update")
py/core/database/graphs.py:            FUSEException: If specific entities were requested but not all found
py/core/database/graphs.py:                raise FUSEException(
py/core/database/graphs.py:            raise FUSEException(status_code=400, message="No fields to update")
py/core/database/graphs.py:            FUSEException: If specific relationships were requested but not all found
py/core/database/graphs.py:                raise FUSEException(
py/core/database/graphs.py:            raise FUSEException(status_code=400, message="No fields to update")
py/core/database/graphs.py:            raise FUSEException(
py/core/database/graphs.py:            raise FUSEException(status_code=400, message="No fields to update")
py/core/database/graphs.py:                raise FUSEException(status_code=404, message="Graph not found")
py/core/database/graphs.py:            FUSEException: If graph not found
py/core/database/graphs.py:            raise FUSEException(f"Graph {graph_id} not found", 404)
py/core/database/graphs.py:            raise FUSEException(
py/core/database/chunks.py:    FUSEException,
py/core/database/chunks.py:        raise FUSEException(
py/core/database/conversations.py:from core.base import Handler, Message, FUSEException
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:                raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/conversations.py:                raise FUSEException(
py/core/database/conversations.py:            raise FUSEException(
py/core/database/users.py:from core.base.abstractions import FUSEException
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:        except FUSEException as e:
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:        except FUSEException:
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:                raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="No users found")
py/core/database/users.py:            raise FUSEException(status_code=404, message="User not found")
py/core/database/users.py:            raise FUSEException(
py/core/database/users.py:            raise FUSEException(status_code=404, message="API key not found")
py/core/database/users.py:            raise FUSEException(status_code=404, message="API key not found")
py/core/database/collections.py:    FUSEException,
py/core/database/collections.py:                raise FUSEException(
py/core/database/collections.py:            raise FUSEException(
py/core/database/collections.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/collections.py:            raise FUSEException(status_code=400, message="No fields to update")
py/core/database/collections.py:                raise FUSEException(
py/core/database/collections.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/collections.py:            FUSEException: If the collection doesn't exist.
py/core/database/collections.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/collections.py:            FUSEException: If the collection doesn't exist, if the document is not found,
py/core/database/collections.py:                raise FUSEException(
py/core/database/collections.py:                raise FUSEException(
py/core/database/collections.py:                raise FUSEException(
py/core/database/collections.py:        except FUSEException:
py/core/database/collections.py:            # Re-raise FUSEExceptions as they are already handled
py/core/database/collections.py:            FUSEException: If the collection doesn't exist or if the document is not in the collection.
py/core/database/collections.py:            raise FUSEException(status_code=404, message="Collection not found")
py/core/database/collections.py:            raise FUSEException(
py/core/database/files.py:from core.base import Handler, FUSEException
py/core/database/files.py:            raise FUSEException(
py/core/database/files.py:            raise FUSEException(
py/core/database/files.py:                    raise FUSEException(
py/core/database/files.py:                    raise FUSEException(
py/core/database/files.py:                raise FUSEException(
py/core/database/files.py:                    raise FUSEException(
py/core/database/files.py:            raise FUSEException(
py/core/database/documents.py:    FUSEException,
py/core/database/documents.py:            raise FUSEException(
py/core/base/providers/auth.py:from ..abstractions import FUSEException, Token, TokenData
py/core/base/providers/auth.py:                raise FUSEException(
py/core/base/providers/auth.py:                raise FUSEException(
py/core/base/providers/auth.py:                except FUSEException:
py/core/base/providers/auth.py:            raise FUSEException(
py/core/base/__init__.py:    "FUSEException",
py/core/base/abstractions/__init__.py:    FUSEException,
py/core/base/abstractions/__init__.py:    "FUSEException",
py/core/__init__.py:    "FUSEException",
