FROM python36

ENV APP_ROOT /home
WORKDIR ${APP_ROOT}/
COPY requirements.txt ${APP_ROOT}/
RUN pip install --no-cache-dir -r requirements.txt
COPY . ${APP_ROOT}

EXPOSE 5000

CMD ["python3", "server_async.py"]
