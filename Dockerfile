FROM python

SHELL ["/bin/bash", "-c"]

RUN pip install --upgrade pip

RUN useradd -rms /bin/bash app && chmod 777 /opt /run

WORKDIR /app

RUN mkdir /app/static && mkdir /app/media && chown -R app:app /app && chmod 775 /app

COPY --chown=app:app . .

RUN pip install -r requirements.txt

USER app

CMD ['python', 'manage.py', 'runserver']