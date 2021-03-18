f = open("C:/Users/student.MCALAB/Desktop/20mca009/cars.csv", "a")
import json
thisdict = {
    "brand":"ford",
    "model":"mustang",
    "year":"1964"
    }
result =json.dumps(thisdict)
f.write(result)
f.close()
f = open("C:/Users/student.MCALAB/Desktop/20mca009/cars.csv", "r")
print(f.read())
