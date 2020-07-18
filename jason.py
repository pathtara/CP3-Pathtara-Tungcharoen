import json
def readJson():
    # ข้อมูล JSON ที่เราต้องการอ่าน
    x =  { "name":"John", "age":30, "city":"New York"}
    # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
    y = json.loads(x)
    # ทำการเรียกข้อมูล age ออกมาแสดง
    print(y["age"])
readJSON()

import json
    
def writeJson():
    # สร้างข้อมูลที่เราต้องการแปลง(ประเภท dictionary)
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }
    # คำสั่งที่ใช้ในการแปลง
    y = json.dumps(x)
    # มาลองดูผลลัพธ์กัน
    print(y)
    
writeJson()