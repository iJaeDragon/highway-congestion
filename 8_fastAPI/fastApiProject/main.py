from fastapi import FastAPI
from fastapi.responses import HTMLResponse
# pip install jinja2
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from fastapi.staticfiles import StaticFiles

from scheduler import start_scheduler, stop_scheduler

# FastAPI 인스턴스 생성
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# 템플릿 설정
templates = Jinja2Templates(directory="templates")

# 스케줄러 시작
start_scheduler()

# FastAPI 애플리케이션 종료 시 스케줄러 중지
@app.on_event("shutdown")
def shutdown_event():
    stop_scheduler()


# 웹 페이지 반환 엔드포인트
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "Welcome to FastAPI!"})


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}