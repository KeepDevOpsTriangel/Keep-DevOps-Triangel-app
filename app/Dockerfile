# Image docker python base for flask app
FROM python:3.10
# Workdir default for aplication
WORKDIR /src
# Copy files for app
COPY src .
COPY requirements.txt .
# Install and update pip and install python-dotenv
# for use .env file
RUN python -m pip install --upgrade pip && \
    pip install python-dotenv && \
    pip install cryptography
# Install requirements for app
RUN pip install -r requirements.txt
# Expose port for flask app
EXPOSE 5000
# main file for flask app
ENV FLASK_APP=app.py
# Run flask app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
