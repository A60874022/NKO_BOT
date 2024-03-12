from mongoengine import connect
from starlette_admin import DropDown
from starlette_admin import I18nConfig
from starlette_admin.contrib.mongoengine import Admin
from starlette_admin.views import Link

from admin.app_admin.config import config
from admin.app_admin.mongoengine.models import Topic
from admin.app_admin.mongoengine.views import TopicView

__all__ = ["admin", "connection"]

connection = connect(host=config.mongo_uri)

admin = Admin(
    "Admin",
    base_url="/admin",
    route_name="admin",
    templates_dir="templates/admin/mongoengine",
    i18n_config=I18nConfig(language_switcher=["ru", "en"]),
)

admin.add_view(
    DropDown(
        label="База данных НКО НЖКЦ",
        icon="fa fa-store",
        views=[TopicView(Topic), ],
    )
)

admin.add_view(Link(label="На страницу приветствия", 
                    icon="fa fa-link", url="/"))
