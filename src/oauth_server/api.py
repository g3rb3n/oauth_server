import logging
from typing import List

from fastapi import APIRouter, Header, Query, status
from fastapi.responses import RedirectResponse, HTMLResponse

from oauth_server import core
from oauth_server import settings
from oauth_server.models import ApiError, Code, Configuration


logger = logging.getLogger(__name__)

router = APIRouter()

responses = {
    500: {'model': ApiError},
}


@router.get('/initialize',
    response_model=Code,
    response_model_exclude_none=True,
    responses=responses)
async def get_code():
    """
    Get a code.
    """
    code = core.initialize({
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'scope': settings.SCOPE,
    })
    return {
        'code': code
    }


@router.post('/initialize',
    response_model=Code,
    response_model_exclude_none=True,
    responses=responses)
async def post_code(data: Configuration):
    """
    Get a code.
    """
    code = core.initialize(data)
    return {
        'code': code
    }


@router.get('/callback',
    response_model=Code,
    response_model_exclude_none=True,
    responses=responses)
async def callback(code: str):
    """
    Callback.
    """
    return {
        'code': core.callback(code)
    }


@router.get('/{code}',
    response_model_exclude_none=True,
    responses=responses)
async def auth_flow(code: str):
    """
    Start auth flow.
    """
    redirect_url = core.get_redirect_url(code)
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@router.get('/code/{code}',
    response_model=Code,
    response_model_exclude_none=True,
    responses=responses)
async def get_token(code: str):
    """
    Get a token.
    """
    token = core.get_code(code)
    return {
        'code': token
    }
