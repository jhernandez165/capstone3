# Stage 1: Build the Angular application
FROM node:14.21.3-bullseye AS builder

# Set the working directory in the Docker image
WORKDIR /app

# Copy package.json and package-lock.json to work directory
COPY package.json package-lock.json ./

# Install all the dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the application
RUN npm run build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-bullseye

# Make sure the path after /app/dist/ matches the directory name where Angular puts the build files
# It's often /app/dist/<project-name>
COPY --from=builder /app/dist/aline-member-dashboard /usr/share/nginx/html

# Copy the nginx configuration file
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# Expose port 4200
EXPOSE 4200

# Start Nginx when the container has provisioned.
CMD ["nginx", "-g", "daemon off;"]
