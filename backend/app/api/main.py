from fastapi import APIRouter
from fastapi import FastAPI

# Importa las rutas
from backend.app.api.routes import items, login, private, users, utils
from app.core.config import settings

# Crea la instancia de FastAPI
app = FastAPI()

# Crea el router principal para las rutas
api_router = APIRouter()

# Incluye las rutas específicas en el router
api_router.include_router(login.router)
api_router.include_router(users.router)
api_router.include_router(utils.router)
api_router.include_router(items.router)

# Solo incluye el router privado si está en el entorno local
if settings.ENVIRONMENT == "local":
    api_router.include_router(private.router)

# Finalmente, incluye el router en la app
app.include_router(api_router)




