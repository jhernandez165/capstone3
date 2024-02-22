# Use a builder image with Maven to build the Java project
FROM maven:3.9.6-eclipse-temurin-17 as builder
WORKDIR /app

# Copy the project files into the image
COPY . .

# Package the application without running tests for the build stage
RUN mvn clean package -DskipTests

# Use the OpenJDK image for the runtime
FROM openjdk:17-jdk-slim

# Set a working directory inside the container
WORKDIR /app

# Copy the JAR file from the builder stage into the production image
COPY --from=builder ./underwriter-microservice/target/underwriter-microservice-0.1.0.jar /app/underwriter-microservice.jar


# Expose the port the microservice runs on
EXPOSE 8070

# Set the environment variable for Spring's active profile
ENV SPRING_PROFILES_ACTIVE=docker

# Command to run the microservice
ENTRYPOINT ["java", "-jar", "/app/user-microservice.jar"]
