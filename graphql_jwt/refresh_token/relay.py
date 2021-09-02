import graphene

from . import mixins
from ..settings import jwt_settings


class Revoke(mixins.RevokeMixin, graphene.ClientIDMutation):
    class Input:
        if not jwt_settings.JWT_HIDE_REFRESH_TOKEN_FIELD and jwt_settings.JWT_LONG_RUNNING_REFRESH_TOKEN:
            refresh_token = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, *args, **kwargs):
        return cls.revoke(*args, **kwargs)


class DeleteRefreshTokenCookie(
    mixins.DeleteRefreshTokenCookieMixin,
    graphene.ClientIDMutation,
):
    @classmethod
    def mutate_and_get_payload(cls, *args, **kwargs):
        return cls.delete_cookie(*args, **kwargs)
