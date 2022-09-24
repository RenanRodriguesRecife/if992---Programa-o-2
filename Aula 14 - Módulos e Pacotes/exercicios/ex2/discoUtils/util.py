import json

class Write():
    def __init__(self):
        pass
        
    def write(self,entity):
       with open(f"{type(entity).__name__}_{entity.id}.json","w") as f:
            json.dump(entity.toJson(),f)

            
class Reader():
    def __init__(self):
        pass
    def read(self,file_name):
        with open(file_name,"r") as file:
            json_object = json.load(file)

        print(json_object)
        return json_object
