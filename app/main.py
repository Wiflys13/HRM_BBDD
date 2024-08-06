#main.py
#iniciar el servidor: uvicorn main:app --reload
# Url local: 127.0.0.1:8000/url
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
from fastapi import FastAPI
from routers import components

app = FastAPI()

@app.get("/")
async def root():
    return "Hola Harmoni"

app.include_router(components.router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
    
    