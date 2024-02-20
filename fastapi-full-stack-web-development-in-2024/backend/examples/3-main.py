from fastapi import Depends, FastAPI, HTTPException
from fastapi.testclient import TestClient


app = FastAPI()


def di_check_id_or_404(id: int):
    if id == 0:
        raise HTTPException(detail=f"{id}", status_code=494)

    return id


def check_id_or_404(id: int):
    if id == 0:
        raise HTTPException(detail=f"The {id} is not allowed", status_code=404)

    return id


@app.get("/one/{id}")
def get_user_by_id_func(id: int = Depends(check_id_or_404)):
    return f"The id func is: {id}"


class CheckId:
    def __call__(self, id: int) -> int:
        if id == 0:
            raise HTTPException(detail=f"The {id} is not allowed", status_code=405)
        return id


@app.get("/two/{id}")
def get_user_by_id_class(id: int = Depends(CheckId())):
    return f"The id class is: {id}"


client = TestClient(app)

app.dependency_overrides[check_id_or_404] = di_check_id_or_404


def test_dependency_injection():
    response = client.get("/one/4")
    assert response.status_code == 200
    assert response.text == '"The id func is: 4"'


def test_dependency_injection_error():
    response = client.get("/one/0")
    assert response.status_code == 494
    assert response.json() == {"detail": "0"}
