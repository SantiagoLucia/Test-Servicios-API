from fastapi import FastAPI
from routers import test_hml, test_prod
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(test_hml.router)
app.include_router(test_prod.router)

@app.get('/test_servicios')
def root():
    return {'endpoints test':['/test_hml','/test_prod']}