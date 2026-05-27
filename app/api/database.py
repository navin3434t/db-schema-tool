from fastapi import APIRouter

from app.models.database import (
    DBConnectionRequest,
    ExecuteSchemaRequest
)

from app.services.database_service import DatabaseService

router = APIRouter(
    prefix="/database",
    tags=["Database"]
)


@router.post("/test-connection")
def test_connection(request: DBConnectionRequest):

    return DatabaseService.test_connection(request)


@router.post("/execute-schema")
def execute_schema(request: ExecuteSchemaRequest):

    return DatabaseService.execute_schema(request)