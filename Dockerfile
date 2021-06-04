# Dockerfile
# Django 최상위 루트에서 작성
FROM python:3.8
# 컨테이너 내에서 코드가 실행될 경로 설정
WORKDIR /usr/src/app
# requirements.txt에 명시된 필요한 packages 설치
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Project를 /usr/src/app으로 복사
COPY . .
# 포트 설정
EXPOSE 8000
# gunicorn 실행
CMD ["gunicorn", "coco.wsgi:application" ,"--bind", "0.0.0.0:8000"]
# EXPOSE, CMD는 docker-compose에서 작성할 것이기 때문에, 동작하는지만 확인 후 주석or삭제 하도록 하자.