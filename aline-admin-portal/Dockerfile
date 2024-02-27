# Stage 1: Build the application
FROM node:14.21.3-bullseye AS build-stage

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Build the app
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-bullseye

# Remove the default Nginx configuration file
RUN rm /etc/nginx/conf.d/default.conf

# Copy the nginx configuration file
COPY /nginx/nginx.conf /etc/nginx/conf.d

# Copy the build output to replace the default nginx contents.
COPY --from=build-stage /app/build /usr/share/nginx/html

# Expose port 3007
EXPOSE 3007

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]
