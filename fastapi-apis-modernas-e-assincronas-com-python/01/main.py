from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi import Path, Query, Header
from model import Course
from typing import Any, List, Dict
from fastapi import Depends


def fake_db():
    try:
        print("Opening database...")
    finally:
        print("Closing database...")


class HTTPNotFoundException(HTTPException):
    def __init__(self, entity: str, id: int):
        detail = f"{entity} {id} not found"
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)


app = FastAPI(
    title="Cursos Service",
    description="API de consulta de cursos",
    version="1.2.2",
)


@app.get(
    "/courses",
    description="Lista de cursos",
    summary="Retorna todos os cursos ativos",
    response_model=List[Course],
    response_description="Cursos encontrados com sucesso."
)
async def get_courses():
    return courses


@app.get("/courses/{id:int}", response_model=Course)
async def get_course_by_id(
    id: int = Path(
        title="ID do curso",
        description="Deve ser entre 1 e 2",
        le=3,
        ge=0,
    )
):
    try:
        course = courses[id]
        return course
    except KeyError:
        raise HTTPNotFoundException("Course", id)


@app.get("/courses/{title:str}")
async def get_course_by_title(
    title: str = Path(title="Título", description="Informe o título do livro"),
    order: str = Query(
        default="desc",
        title="Ordering",
        description="Retornar a order da listagem",
    ),
    x_cache_age: int = Header(
        default=None, title="Cache Age", description="Idade do cache em dias"
    ),
    db: Any = Depends(fake_db),
):
    """
    curl  -X GET \
        'http://0.0.0.0:8000/courses/python/?order=asc' \
        --header 'x-cache-age: 40423'
    """
    return {
        "title": title,
        "order": order,
        "cache_age": x_cache_age,
    }


@app.post("/courses", status_code=status.HTTP_201_CREATED, response_model=Course)
def create_course(course: Course):
    _id = max(courses.keys()) + 1
    courses[_id] = course
    return course


@app.put("/courses/{id:int}", response_model=Course)
def update_course(id: int, course: Course):
    if id not in courses:
        raise HTTPNotFoundException("Course", id)

    courses[id] = course
    return courses[id]


@app.delete("/courses/{id:int}", status_code=status.HTTP_204_NO_CONTENT)
def remove_course(id: int):
    if id not in courses:
        raise HTTPNotFoundException("Course", id)

    del courses[id]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
