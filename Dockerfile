FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV TZ=Europe/Istanbul
WORKDIR /app
COPY requirement.txt ./
RUN apt update
RUN apt install nano
RUN python -m pip install --upgrade pip
RUN pip install gunicorn
RUN pip install -r requirement.txt
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY ./ /app
