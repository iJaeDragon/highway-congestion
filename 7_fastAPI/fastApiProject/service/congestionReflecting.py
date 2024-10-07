from script import yoloV8

from script import statusUpdate

def reflecting() :
    results = yoloV8.detect()  # 감지 메서드 호출
    print(results)

    curStatus = ""
    if(results["count"] < 20) :
        curStatus = "1"
    elif(results["count"] >= 20 and results["count"] < 30) :
        curStatus = "2"
    else:
        curStatus = "3"


    statusUpdate.update_status('ED0001', curStatus)
