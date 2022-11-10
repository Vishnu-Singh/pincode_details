from decouple import config
import motor.motor_asyncio
mongo_url = config("MONGODB_URL")
print(mongo_url)
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
db = client.pincode_details