
FROM ubuntu:20.04
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app 
ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=Asia/Kolkata 
RUN apt -qq update --fix-missing && apt -qq upgrade
RUN apt -qq install -y ffmpeg python3-pip
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
