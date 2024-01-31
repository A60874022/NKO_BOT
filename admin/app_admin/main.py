from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from .config import config
from app_admin.mongoengine import admin as admin_mongo


async def homepage(request):
    return Jinja2Templates("templates").TemplateResponse(
        "index.html", {"request": request, "config": config}
    )


app = Starlette(
    routes=[
        Route("/", homepage),
        Mount("/statics", app=StaticFiles(directory="statics"),
              name="statics"),
    ]
)
admin_mongo.mount_to(app)
