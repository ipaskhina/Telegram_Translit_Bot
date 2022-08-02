FROM python:slim
ENV TOKEN='5361230442:AAGOvU1wUbRIslf9F2waXA2cOxwMfHo-8SI'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py

