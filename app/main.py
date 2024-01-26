from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from api.contact_items import router as contact_router
from api.users import router as user_router
from models import contact
from depenedencies.database import engine

contact.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(contact_router, prefix="/contact")
app.include_router(user_router, prefix="/users")


@app.get("/")
async def health_check():
    print()
    return {"OK": True}


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
