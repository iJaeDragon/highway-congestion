from apscheduler.schedulers.background import BackgroundScheduler

from script import statusUpdate

from script import yoloV8

from service import congestionReflecting

# 스케줄러 인스턴스 생성
scheduler = BackgroundScheduler()

# 작업 정의
def scheduled_task():
    congestionReflecting.reflecting()

# 작업 추가
def start_scheduler():
    scheduler.add_job(scheduled_task, 'interval', seconds=10)
    scheduler.start()

# 스케줄러 중지 함수
def stop_scheduler():
    scheduler.shutdown()