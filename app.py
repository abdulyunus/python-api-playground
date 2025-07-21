# App file for the project.
from flask_openapi3 import Info, OpenAPI, Tag, APIBlueprint


info = Info(
    title="My First Application",
    version="1.0.0",
    description="This is a sample application using OpenAPI3 with Flask.",
)

app = OpenAPI(__name__, info=info, doc_prefix="/api", api_doc_url="/openapi.json")

health_tag = Tag(name="Health", description="Health check endpoints")
router = APIBlueprint("/", __name__, abp_tags=[health_tag], url_prefix="/api")

@app.get("/health", tags=[health_tag])
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok"}, 200

@app.get("/info", tags=[health_tag])
def get_info():
    """
    Endpoint to return application information.
    """
    return {
        "application": "My First Application",
        "version": "1.0.0",
        "description": "This is a sample application using OpenAPI3 with Flask."
    }, 200

# Register the router with the app
app.register_api(router)
if __name__ == "__main__":
    """
    Main entry point to run the Flask application.
    """
    app.run(host="0.0.0", port=8000, debug=True)
