from fastapi import FastAPI
import uvicorn
from decouple import config
from service.pincode_check import Pincode

HOST = config("HOST")
PORT = int(config("PORT"))
pincode_service = Pincode()
print(f"host: {HOST}, type: {type(HOST)}\nport: {PORT} type: {type(PORT)}")

app = FastAPI()

@app.get("/")
def index():
    return "Pincode checker"

@app.get("/check_pincode/{pincode}")
def check_pincode(pincode):
    details = pincode_service.area_details(pincode)
    return details

if __name__ == "__main__":
    uvicorn.run(app,host=HOST,port=PORT)