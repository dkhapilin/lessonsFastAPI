from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from auth.auth import auth_backend
from auth.database import User, get_async_session
from auth.manager import get_user_manager
from auth.shemas import UserRead, UserCreate
from models.models import salary

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()

app = FastAPI(
    title='lessonsFastAPI'
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/login",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


@app.get("/salary")
async def show_salary(q_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    query = select(salary).where(salary.c.user_id == q_user.id)
    result = await session.execute(query)
    answer = result.fetchall()
    return {"salary": answer[0][0],
            "data_salary": answer[0][1]}
