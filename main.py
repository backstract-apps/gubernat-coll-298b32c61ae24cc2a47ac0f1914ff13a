from fastapi import FastAPI
from database import engine
import models
import uvicorn
from routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Backstract Generated APIs - gubernat-coll-298b32c61ae24cc2a47ac0f1914ff13a',debug=False,docs_url='/bold-mayer-af0cbaac9c1311efb0410242c0a8900371/docs',openapi_url='/bold-mayer-af0cbaac9c1311efb0410242c0a8900371/openapi.json')

app.include_router(router, prefix='/bold-mayer-af0cbaac9c1311efb0410242c0a8900371/api', tags=['APIs v1'])

def run_h11():
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)

if __name__ == '__main__':
    run_h11()