
FROM ubuntu:20.04
WORKDIR /usr/src/app
RUN chmod 777 /usr/src/app 
ENV DEBIAN_FRONTEND=noninteractive 
ENV TZ=Asia/Kolkata 
RUN apt -qq install -y ffmpeg
COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
CMD ["bash","start.sh"]
