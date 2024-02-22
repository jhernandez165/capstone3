# Stage 1: Build the React application
FROM node:14.21.3 as build

WORKDIR /app

COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the application from Nginx
FROM nginx:stable-alpine

# Copy the build artifacts from the build stage to the Nginx directory
COPY --from=build /app/build /usr/share/nginx/html

# Expose the port Nginx is listening on
EXPOSE 80

# Start Nginx when the container has launched
CMD ["nginx", "-g", "daemon off;"]
