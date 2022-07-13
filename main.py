from fastapi import FastAPI

app = FastAPI(
    title="weblate-batch-scripts",
    version="0.0.1",
    terms_of_service="https://github.com/samzong/webalte-batch-scripts",
    contact={
        "name": "samzong",
        "url": "https://github.com/samzong",
        "email": "samzong.lu@gmail.com",
        },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
        },
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}
