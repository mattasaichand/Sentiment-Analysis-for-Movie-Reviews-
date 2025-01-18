
# Use a Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /backend

# Install dependencies
COPY ./backend/requirements.txt /backend/requirements.txt
RUN pip install --no-cache-dir -r /backend/requirements.txt

# Copy the backend code
COPY ./backend /backend

# Expose port
EXPOSE 8000

# Start the FastAPI app using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]