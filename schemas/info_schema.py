from pydantic import BaseModel, Field
from typing import List, Optional

# 정보 등록 요청 스키마
class InfoCreate(BaseModel) :
  name:str = Field(
    ...,
    min_length=1,
    description="이름"
  )
  
  phone:str = Field(
    ...,
    min_length=10,
    description="전화번호",
  )
  
  address:str = Field(
    "주소 없음",
    description="주소"
  )
  
  model_config = {
    "json_schema_extra": {
      "example": {
        "name": "홍길동",
        "phone": "01012345678",
        "address": "강남구",
      }
    }
  }
  

# 정보 응답 스키마
class InfoResponse(BaseModel) :
  """
  정보 응답 스키마
  """
  id:int
  name:str
  phone:str
  address:str


# 정보 수정 스키마
class InfoUpdate(BaseModel) :
  """
  정보 수정 스키마
  """
  name:Optional[str] = None
  phone:Optional[str] = None
  address:Optional[str] = None