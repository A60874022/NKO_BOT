import uvicorn
from fastapi import FastAPI
from starlette_admin.contrib.mongoengine import Admin, ModelView
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware
from contextlib import asynccontextmanager
from .provider import MyAuthProvider, pwd_context
from starlette_admin.i18n import set_locale
from mongoengine import connect, disconnect

from .models import User, Topic
from .settings import MONGO_URL, SECRET, MONGO_INITDB_ROOT_USERNAME, MONGO_INITDB_ROOT_PASSWORD


set_locale("ru")


@asynccontextmanager
async def lifespan(app: FastAPI):
    connect(host=MONGO_URL)
    user = User(name=MONGO_INITDB_ROOT_USERNAME, password=pwd_context.hash(MONGO_INITDB_ROOT_PASSWORD))
    user.save()
    yield
    user.delete()
    disconnect()


app = FastAPI(lifespan=lifespan)

admin = Admin(
    title="Chatbot Admin panel",
    base_url="/",
    auth_provider=MyAuthProvider(),
    middlewares=[Middleware(SessionMiddleware, secret_key=SECRET)],
)


class UserView(ModelView):
    label = "Администраторы"
    name = "Администратор"
    exclude_fields_from_list = ["password"]
    fields_default_sort = [(User.name, True)]

    async def before_create(self, request, data, user):
        user.password = pwd_context.hash(data["password"])

    async def before_edit(self, request, data, user):
        user.password = pwd_context.hash(data["password"])



class TopicView(ModelView):
    label = "НКО-БОТ"
    name = "НКО-БОТ"

admin.add_view(UserView(User))

admin.add_view(TopicView(Topic))


admin.mount_to(app)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000)
