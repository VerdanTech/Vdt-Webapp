# Standard Library
import uuid
from datetime import datetime
from enum import Enum
from functools import partial

# External Libraries
from jose import JWTError, jwt
from litestar.datastructures import Cookie
from pydantic import UUID4, BaseModel

# VerdanTech Source
from src import exceptions, settings


class TokenTypeEnum(Enum):
    """
    Two types of JWT tokens are used in the application:

    Access tokens are short lived and are used to grant
    access to the application resources. Refresh tokens
    are long lived and are used to grant access tokens.

    Tokens are rotated frequently to enhance security.

    The string value of the enum is used as the key
    in the cookie for token storage.
    """

    ACCESS = "accessToken"
    REFRESH = "refreshToken"


class Token(BaseModel):
    exp: datetime
    iat: datetime
    sub: UUID4


token_settings = {
    TokenTypeEnum.ACCESS: {
        "secret": settings.ACCESS_JWT_SECRET,
        "expiry_timedelta": settings.ACCESS_JWT_EXPIRY_TIMEDELTA,
        "algorithm": settings.ACCESS_JWT_ALGORITHM,
    },
    TokenTypeEnum.REFRESH: {
        "secret": settings.REFRESH_JWT_SECRET,
        "expiry_timedelta": settings.REFRESH_JWT_EXPIRY_TIMEDELTA,
        "algorithm": settings.REFRESH_JWT_ALGORITHM,
    },
}


def _decode_jwt_token(encoded_token: str, token_type: TokenTypeEnum) -> Token:
    """
    Helper function that decodes a jwt token.
    If the token is invalid or expired an exception is raised.

    Args:
        encoded_token (str): the JWT token before decoding.
        token_type (TokenTypeEnum): whether the toke to be decoded
            is an access or refresh token.

    Raises:
        AuthenticationError: If the JWT token is invalid.
    """
    try:
        payload = jwt.decode(
            token=encoded_token,
            key=token_settings[token_type]["secret"],
            algorithms=token_settings[token_type]["algorithm"],
        )
        return Token(**payload)
    except JWTError:
        raise exceptions.AuthenticationError()


def _encode_jwt_token(user_id: uuid.UUID, token_type: TokenTypeEnum) -> str:
    """
    Helper function that encodes a JWT token.

    Args:
        user_id (uuid.UUID): the ID of the user is used to
            create the jwt key string
        token_type (TokenTypeEnum): whether the toke to be encoded
            is an access or refresh token.
    """
    token = Token(
        exp=datetime.now() + token_settings[token_type]["expiry_timedelta"],
        iat=datetime.now(),
        sub=user_id,
    )
    return jwt.encode(
        token.model_dump(),
        token_settings[token_type]["secret"],
        algorithm=token_settings[token_type]["algorithm"],
    )


def _token_to_cookie(token: str, token_type: TokenTypeEnum) -> Cookie:
    if settings.CLIENT_SAMESITE:
        cookie_samesite = "strict"
    else:
        cookie_samesite = "lax"

    return Cookie(
        key=token_type.value,
        value=token,
        httponly=True,
        secure=settings.USING_HTTPS,
        samesite=cookie_samesite,
        expires=token_settings[token_type]["expiry_timedelta"].total_seconds(),
    )


decode_access_token = partial(_decode_jwt_token, token_type=TokenTypeEnum.ACCESS)
decode_refresh_token = partial(_decode_jwt_token, token_type=TokenTypeEnum.ACCESS)
encode_access_token = partial(_encode_jwt_token, token_type=TokenTypeEnum.REFRESH)
encode_refresh_token = partial(_encode_jwt_token, token_type=TokenTypeEnum.REFRESH)
access_token_to_cookie = partial(_token_to_cookie, token_type=TokenTypeEnum.ACCESS)
refresh_token_to_cookie = partial(_token_to_cookie, token_type=TokenTypeEnum.REFRESH)
