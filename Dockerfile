FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Fix vulnerability that affects denial of service attacks
RUN apt-get update && apt-get install -y openssl && apt-get upgrade -y openssl

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the source code
COPY . .

# Run Django migrations
RUN python manage.py makemigrations && python manage.py migrate

# Expose the application's port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]