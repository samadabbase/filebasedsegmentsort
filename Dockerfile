FROM python:3.9
WORKDIR /app
# Copy only the necessary files
COPY . /app
EXPOSE 80
CMD ["python", "scalable_consumer.py"]
