from pydantic import BaseModel


class DBConnectionRequest(BaseModel):
    db_type: str
    host: str
    port: int
    username: str
    password: str
    database: str


class ExecuteSchemaRequest(DBConnectionRequest):
    schema_script: str