from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from admin.app_admin.config import config
from admin.app_admin.mongoengine import admin as admin_mongo


async def homepage(request):
    return Jinja2Templates("admin/templates").TemplateResponse(
        "index.html", {"request": request, "config": config}
    )


app = Starlette(
    routes=[
        Route("/", homepage),
        Mount("/statics", app=StaticFiles(directory="admin/statics"),
              name="statics"),
    ]
)
admin_mongo.mount_to(app)
