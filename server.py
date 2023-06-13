from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Creating the app
app = FastAPI()


#  Allowing the react app to communicate with the backend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"msg": "Hello World i am fast"}
