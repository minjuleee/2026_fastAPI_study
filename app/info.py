# 이름, 전화번호, 주소를 CRUD 할 수 있는 fastAPI 흉내 내보기
# 이름, 전화번호는 필수. 주소는 optional
# 최대한... vibe 없이 해보시기 바래요~!
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import List, Optional
from schemas.info_schema import InfoCreate, InfoResponse


app = FastAPI(
    title="회원정보관리 API",
    description="FastAPI 기초 실습 - 회원정보관리 CRUD를 할 수 있는 엔드포인트",
    version="1.0.0"
)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

info_db:dict = {}
info_id = 1


# 서버 상태 확인용 API
@app.get("/health", summary="서버 상태 확인", tags=["시스템"])
def health_check() : 
  """
  서버 상태 체크
  """
  return {"status" : "ok", "version": "1.0.0"}


# 정보등록 (POST /info)
@app.post("/info", response_model=InfoResponse, status_code=201, tags=["정보"])
def create_info(info:InfoCreate) :
  """
  정보를 등록합니다.
  status_code=201 : 생성 성공을 의미하는 HTTP 코드
  """
  global info_id
  record = {"id" : info_id, **info.model_dump()}
  
  info_db[info_id] = record
  info_id += 1
  return record
  
  