"""
FastAPI main for Twitter SMPS
"""

import logging
import uvicorn

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from oauth_server import api
from oauth_server.utils import setup_app, include


logger = logging.getLogger(__name__)


app = setup_app()
include(app, api, '')


def log_request_exception(request, exception):
    """
    Log request exception.
    """
    logger.error(request.url)
    logger.error(exception)



@app.exception_handler(Exception)
async def exception_handler(request, exception) -> JSONResponse:
    """
    Respond with a 500 if an exception occurs.
    """
    log_request_exception(request, exception)
    return JSONResponse(
        status_code=500,
        content={
            'error': str(exception),
            'message': 'Internal server error'
        }
    )

if __name__ == '__main__':
    uvicorn.run(app, port=8888, host='0.0.0.0')
