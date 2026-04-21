from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import app.api.routes as routes

app = FastAPI(title="Resume AI Screener")
app.include_router(routes.router, prefix="/api")


def _swagger_file_schema_compat(schema: object) -> None:
    """Convert OpenAPI 3.1 file fields to Swagger UI friendly 3.0-style binary format."""
    if isinstance(schema, dict):
        if schema.get("type") == "string" and schema.get("contentMediaType") == "application/octet-stream":
            schema.pop("contentMediaType", None)
            schema["format"] = "binary"
        for value in schema.values():
            _swagger_file_schema_compat(value)
    elif isinstance(schema, list):
        for item in schema:
            _swagger_file_schema_compat(item)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description=app.description,
        routes=app.routes,
    )
    _swagger_file_schema_compat(openapi_schema)
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

print("App loaded")