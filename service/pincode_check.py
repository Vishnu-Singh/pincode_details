# from utils.mongo_connection import db
from models.pincode_details import RegionCode,StateRegion
from utils.pincode_keys import get_pincode_details,first_two_digit_meaning
import json

class Pincode():

    def __init__(self):
        resion_code = RegionCode()
        stateRegion = StateRegion()

    def check_validation(self):
        pincode_validat = get_pincode_details("000000")
        if pincode_validat[0] and pincode_validat[1]:
            print("valid pincode")
        else:
            print("not valid")

    def area_details(self,pincode:str):
        details = get_pincode_details(pincode)
        # details = {
        #     "Region":[state for state in details[0]],
        #     "states":details[1]
        # }
        print(details)
        details = json.dumps(details)

        return details