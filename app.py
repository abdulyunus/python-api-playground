from pydantic import BaseModel
from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI

Info = Info(
    title="My First Application",
    version="0.1",
    description="First application using the FlaskOpenAPI3 API",
)
app = OpenAPI(__name__, info=Info)

book_tag = Tag(name="Book", description="Book API")


class BookQuery(BaseModel):
    age: int
    auther: str


@app.get("/book", tags=[book_tag], responses={"200": BookQuery}, summary="Book API")
def get_book(query: BookQuery):
    """
    Get book details based on the query parameters.
    """
    return {"age": query.age, "auther": query.auther}


if __name__ == "__main__":
    """
    Main entry point to run the Flask application.
    """
    app.run(debug=True)
