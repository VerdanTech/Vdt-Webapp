# Standard Library
import uuid
from datetime import datetime, timedelta
from enum import Enum
from functools import partial

# External Libraries
from jose import JWTError, jwt
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
    """

    ACCESS = "access"
    REFRESH = "refresh"


class Token(BaseModel):
    exp: datetime
    iat: datetime
    sub: UUID4


def _get_token_settings(token_type: TokenTypeEnum) -> tuple[str, timedelta, str]:
    """
    Given a token type, returns the settings for the token.
    This includes the secret, the expiry, and the algorithm.

    Args:
        token_type (TokenTypeEnum): the type of token to get the settings for.

    Raises:
        exceptions.DomainIntegrityException: Raised if a value of
            TokenTypeEnum was passed that was unmapped

    Returns:
        tuple[str, timedelta, str]: the secret value used for encoding/decoding,
            the expiry timedelta, and the algorithm used for encoding/decoding.
    """
    match token_type:
        case TokenTypeEnum.ACCESS:
            return (
                settings.ACCESS_JWT_SECRET,
                settings.ACCESS_JWT_EXPIRY_TIMEDELTA,
                settings.ACCESS_JWT_ALGORITHM,
            )
        case TokenTypeEnum.REFRESH:
            return (
                settings.REFRESH_JWT_SECRET,
                settings.REFRESH_JWT_EXPIRY_TIMEDELTA,
                settings.REFRESH_JWT_ALGORITHM,
            )
        case _:
            raise exceptions.DomainIntegrityException(
                "Unmapped value of TokenTypeEnum within _get_token_settings"
            )


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
    secret, expiry_timedelta, algorithm = _get_token_settings(token_type)
    try:
        payload = jwt.decode(token=encoded_token, key=secret, algorithms=[algorithm])
        return Token(**payload)
    except JWTError as e:
        raise exceptions.AuthenticationError(
            f"JWT failed to parse with an error {e}",
            non_form_errors=["Failed to parse incoming JWT Token"],
        )


def _encode_jwt_token(user_id: uuid.UUID, token_type: TokenTypeEnum) -> str:
    """
    Helper function that encodes a JWT token.

    Args:
        user_id (uuid.UUID): the ID of the user is used to
            create the jwt key string
        token_type (TokenTypeEnum): whether the toke to be encoded
            is an access or refresh token.
    """
    secret, expiry_timedelta, algorithm = _get_token_settings(token_type)
    token = Token(
        exp=datetime.now() + expiry_timedelta,
        iat=datetime.now(),
        sub=user_id,
    )
    return jwt.encode(token.model_dump(), secret, algorithm=algorithm)


decode_access_token = partial(_decode_jwt_token, token_type=TokenTypeEnum.ACCESS)
decode_refresh_token = partial(_decode_jwt_token, token_type=TokenTypeEnum.ACCESS)
encode_access_token = partial(_encode_jwt_token, token_type=TokenTypeEnum.REFRESH)
encode_refresh_token = partial(_encode_jwt_token, token_type=TokenTypeEnum.REFRESH)
