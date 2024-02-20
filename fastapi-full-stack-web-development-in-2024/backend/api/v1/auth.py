from typing import Annotated, Any

from fastapi import APIRouter, Cookie, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from backend.core.auth import create_access_token, get_token_payload
from backend.core.hashing import verify_password
from backend.db.repository.user import get_user_by_email
from backend.db.session import get_db
from backend.schemas.auth import TokenResponse, TokenUserResponse


router = APIRouter()


@router.post(
    "/login", response_model=TokenResponse, status_code=status.HTTP_201_CREATED
)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
):
    db_user = get_user_by_email(form_data.username, db)

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password"
        )

    access_token = create_access_token(db_user)
    refresh_token = ""

    return TokenResponse(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )
    # https://www.oauth.com/oauth2-servers/access-tokens/access-token-response/
    # https://github.com/tiangolo/fastapi/discussions/9601


@router.get(
    "/me",
    response_model=TokenUserResponse,
)
def get_me(payload: Annotated[Any, Depends(get_token_payload)]):
    breakpoint()
    expires = payload.get("exp")

    if expires:
        # create a validation expiration time
        pass

    return TokenUserResponse(
        id=payload.get("uid"),
        fullname=payload.get("ufn"),
        email=payload.get("sub"),
    )


@router.get(
    "/me-by-ck",
)
def get_me_by_cookie(access_token: Annotated[str | None, Cookie()] = None):
    return access_token


# @router.post("/logout", response_model=UserLogoutResponse, status_code=status.HTTP_204_NO_CONTENT)
# def logout(db: Session = Depends(get_db)):
#     return


# @router.post("/refresh", response_model=UserRefreshResponse, status_code=HTTP_200_OK)
# def refresh(db: Session = Depends(get_db)):
#     return
