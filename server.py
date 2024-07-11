from fastapi import FastAPI,File, UploadFile
from fastapi.responses import JSONResponse
import utils.openai as open_fns
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/python")
def gen_answer():
    answer = open_fns.gen_answer()
    return answer