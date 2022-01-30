FROM python:3.10-alpine
ENV CRON_SPEC="2 * * * *" 
WORKDIR ./
COPY . ./app
RUN pip install -r ./app/requirements.txt
RUN echo "${CRON_SPEC} python /app/init.py >> /var/log/cron.log 2>&1" > ./app/crontab
RUN crontab ./app/crontab
RUN crontab -l
RUN touch /var/log/cron.log
CMD crond && tail -f /var/log/cron.log