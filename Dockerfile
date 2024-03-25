# 
FROM python:3.10

# 
WORKDIR /rename

# 
COPY ./requirements.txt /rename/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /rename/requirements.txt

# 
COPY ./app /rename/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]