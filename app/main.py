#main.py
# iniciar el servidor: uvicorn main:app --reload o en PS el directorio C:\Users\HARMONI\Documents\HARMONI\HRM_BBDD\app python main.py 
# Url local: 127.0.0.1:8000/url
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
from fastapi import FastAPI
from routers import components, combined, electrical, mechanical, advanced_search


app = FastAPI()

@app.get("/")
async def root():
    return "Hola Harmoni"

app.include_router(components.router)
app.include_router(mechanical.router)
app.include_router(electrical.router)
app.include_router(combined.router)
app.include_router(advanced_search.advanced_search_router)
app.include_router(combined.router)



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)
    
    