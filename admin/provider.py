from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AuthProvider
from starlette_admin.exceptions import LoginFailed
from .models import User
from passlib.context import CryptContext
from .settings import MONGO_URL, SECRET
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class MyAuthProvider(AuthProvider):
    async def login(
        self,
        username: str,
        password: str,
        remember_me: bool,
        request: Request,
        response: Response,
    ) -> Response:
        user = User.objects(name=username)
        if pwd_context.verify(password, user[0].password):
            request.session.update({"username": username})
            return response
        raise LoginFailed("Invalid username or password")

    async def is_authenticated(self, request) -> bool:
        if User.objects(name=request.session.get("username", None)):
            request.state.user = User.objects(name=request.session["username"])
            return True
        return False

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response
