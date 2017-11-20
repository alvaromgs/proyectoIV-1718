FROM python:3

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

ENV PORT 5000
ENTRYPOINT ["python3"]
CMD ["bot/app.py"]

EXPOSE 5000