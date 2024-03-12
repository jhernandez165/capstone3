# Use a builder image with Maven to build the Java project
FROM maven:3.9.6-eclipse-temurin-17 as builder
WORKDIR /app

# Copy the project files into the image
COPY . .

# Package the application without running tests for the build stage
RUN mvn clean package -DskipTests

# Use the OpenJDK image for the runtime
FROM openjdk:11-jre-slim as production

# Set a working directory inside the container
WORKDIR /app

# Copy the JAR file from the builder stage into the production image
COPY --from=builder /app/account-microservice/target/account-microservice-0.1.0.jar /app/account-microservice.jar

# Expose the port the microservice runs on
EXPOSE 8074

# Command to run the microservice
ENTRYPOINT ["java", "-jar", "/app/account-microservice.jar"]
