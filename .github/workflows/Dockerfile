FROM python:3.9-slim
WORKDIR /.github/workflows
COPY . /cs330_04_1.py

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD ["python", "cs330_04_1.py"]
