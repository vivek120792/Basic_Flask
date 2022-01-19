FROM python:3.7
COPY . /user/app/
EXPOSE 5001
WORKDIR /user/app/
RUN pip install -r requirements.txt
CMD python app.py