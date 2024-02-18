from freezegun import freeze_time


@freeze_time("2012-01-14 03:21:34", tz_offset=0)
def test_create_new_user(client):

    data = {
        "fullname": "John Dou",
        "email": "john@john.com",
        "password": "123456",
    }

    response = client.post("/api/v1/user/", json=data)

    assert response.status_code == 201
    
    assert response.json()["id"] == 1

    # assert response.json() == {
    #     "created_at": "2012-01-14T03:21:34",
    #     "email": "john@john.com",
    #     "fullname": "John Dou",
    #     
    #     "is_admin": False,
    # }


@freeze_time("2012-01-14 03:21:34", tz_offset=0)
def test_get_users(client):

    data = {
        "fullname": "John Dou",
        "email": "john@john.com",
        "password": "123456",
    }
    response = client.post("/api/v1/user/", json=data)
    assert response.status_code == 201
    
    data = {
        "fullname": "Julia Fhi",
        "email": "j@j.com",
        "password": "asasdfasd",
    }
    response = client.post("/api/v1/user/", json=data)
    assert response.status_code == 201
    
    response = client.get("/api/v1/user/")
    
    assert response.status_code == 200
    assert len(response.json()) == 2
    
    print(response.json())