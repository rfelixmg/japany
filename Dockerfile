FROM python:3.11-slim

# Install deps
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY . .

EXPOSE 5005
CMD ["python", "app.py"]
