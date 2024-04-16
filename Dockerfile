

FROM python:3.12.0

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
