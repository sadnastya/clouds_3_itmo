FROM python:3.9

COPY requirements.txt .

RUN pip install \
	numpy \
	pandas


COPY matrix.py .

CMD ["python","matrix.py"]

