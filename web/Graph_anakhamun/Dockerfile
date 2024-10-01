# Use an official Node.js runtime as a parent image
FROM node:16-slim

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json files
COPY ./source .


# Install dependencies
RUN npm install

# Expose the port the app runs on
EXPOSE 4000

# Start the app
CMD ["node", "app.js"]
