FROM node:18-alpine

WORKDIR /app

# Copy package files
COPY frontend/package.json ./

# Install dependencies (using npm install instead of ci since we don't have lock file)
RUN npm install

# Copy application code
COPY frontend/ .

# Expose port
EXPOSE 5173

# Default command
CMD ["npm", "run", "dev", "--", "--host"]
