FROM python3.6.3
ENV LANG C.UTF-8
COPY automation.zip /opt/
RUN unzip -d /opt/automation-test /opt/automation.zip
RUN cp -r /opt/automation-test/Django/venv/Lib/site-packages/pytz_deprecation_shim* /usr/local/python/lib/python3.6/site-packages/
RUN cd /opt/automation-test/Django/venv/Lib/site-packages/ && rm -rf dateutil numpy* pandas* pytz* six* python_dateutil*
RUN mv /opt/automation-test/Django/venv/Lib/site-packages/* /usr/local/python/lib/python3.6/site-packages/
WORKDIR /opt/automation-test
ENV LC_ALL="en_US.UTF-8"
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]