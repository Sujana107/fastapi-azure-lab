from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Status": "Success", "Message": "Hello Sujana! Your Azure Web App is working."}
