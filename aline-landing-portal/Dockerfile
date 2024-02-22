# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install app dependencies
RUN npm install

# Bundle app source inside Docker image
COPY . .

# Build the application for production
RUN npm run build

# The port that your app runs on
EXPOSE 3000

# Command to run your app
CMD [ "npm", "start" ]
