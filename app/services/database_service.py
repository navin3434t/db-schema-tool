from sqlalchemy import create_engine, text
from app.core.db_helper import build_connection_string


class DatabaseService:

    @staticmethod
    def test_connection(request):

        try:
            connection_string = build_connection_string(request)
            print(connection_string)
            engine = create_engine(connection_string)

            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            return {
                "success": True,
                "message": "Connection successful"
            }
        except Exception as ex:

            error = str(ex)
            print("DATABASE ERROR:", error)

            return {
                "success": False,
                "message": error
            }

        """except Exception as ex:

            error = str(ex)

            if "Client with IP address" in error:
                return {
                    "success": False,
                    "message": "Azure SQL firewall is blocking this IP. Add the client IP to Azure SQL firewall rules."
                }

            return {
                "success": False,
                "message": error
            }"""

    @staticmethod
    def execute_schema(request):

        try:
            connection_string = build_connection_string(request)

            engine = create_engine(connection_string)

            with engine.connect() as conn:

                statements = [
                    stmt.strip()
                    for stmt in request.schema_script.split(";")
                    if stmt.strip()
                ]

                for statement in statements:
                    conn.execute(text(statement))

                conn.commit()

            return {
                "success": True,
                "message": "Schema executed successfully"
            }

        except Exception as ex:
            return {
                "success": False,
                "message": str(ex)
            }