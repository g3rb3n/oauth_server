FROM python:3.8
WORKDIR /app

COPY Pipfile .
COPY src .

# Install dependencies from Pipfile
RUN pip install pipenv
RUN pipenv install

EXPOSE 8888
CMD ["pipenv", "run", "uvicorn", "oauth_server.main:app", "--reload", "--port", "8888"]
