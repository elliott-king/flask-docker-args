FROM python:3


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Arbitrary build arg
ARG BUILD_ARG
ENV BUILD_ARG $BUILD_ARG

ENTRYPOINT ["python"]
CMD ["web/app.py"]