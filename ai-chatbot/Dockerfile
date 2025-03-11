FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "chatbot.py", "--server.port=8501", "--server.address=0.0.0.0"]
