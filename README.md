# Air-Alarm-SensorServer

##API 
1. dust
  공공데이터포털의 미세먼지 API를 사용하여 미세먼지 데이터를 반환해주는 모듈
  
2. weather
  공공데이터포털의 기상청 제공 API를 사용하여 온습도 데이터를 반환해주는 모듈
  
  
##DB
1. STM32
  STM32를 사용하여 온습도, 미세먼지, Co2 센서값을 받아 반환해주는 모듈

2. insertToDB
  STM32, 각종 API 등에서 받아온 데이터를 전처리 후 DB에 삽입해주는 모듈

3. getFromDB
  DB에 저장된 각종 값들을 시스템에 반환해주는 모듈
  
  
##main

Flask를 사용한 Rest API로, DB에서 받아온 각종 값을 Json 규격으로 웹에 반환해 앱에서 읽어들일 수 있도록 만드는 모듈
