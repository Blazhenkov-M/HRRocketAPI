from fastapi import FastAPI
import uvicorn

from _version import __version__ as service_version

from app.api.api_v1 import router as api_router
from app.core.settings import conf

app = FastAPI(version=service_version,
              redoc_url=None,
              title=conf.app_title,
              swagger_ui_parameters={'displayRequestDuration': True,
                                     'tryItOutEnabled': True})

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run(app, host=conf.host, port=conf.port)
