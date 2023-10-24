FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /news
COPY req.txt /news/
RUN pip install -r req.txt
COPY . /news/

RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "entrypoint.sh"]