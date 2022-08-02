FROM python:slim
ENV TOKEN='insert your TOKEN here'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py

