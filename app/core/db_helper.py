from app.models.database import DBConnectionRequest
from urllib.parse import quote_plus

def build_connection_string(req: DBConnectionRequest):

    db_type = req.db_type.lower()

    if db_type == "mysql":
        return (
            f"mysql+pymysql://{req.username}:{req.password}"
            f"@{req.host}:{req.port}/{req.database}"
        )

    if db_type == "postgresql":
        return (
            f"postgresql+psycopg2://{req.username}:{req.password}"
            f"@{req.host}:{req.port}/{req.database}"
        )

    if db_type == "sqlserver":
        params = quote_plus(
            f"DRIVER={{ODBC Driver 18 for SQL Server}};"
            f"SERVER={req.host},{req.port};"
            f"DATABASE={req.database};"
            f"UID={req.username};"
            f"PWD={req.password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=no;"
        )

        return f"mssql+pyodbc:///?odbc_connect={params}"

    raise ValueError(f"Unsupported database type: {db_type}")