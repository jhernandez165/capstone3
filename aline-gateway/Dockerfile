# Use a builder image with Maven to build the Java project
FROM maven:3.8.1-jdk-11 as builder
WORKDIR /app

# Copy the project files into the image
COPY . .

# Package the application without running tests for the build stage
RUN mvn clean package -DskipTests

# Use the OpenJDK image for the runtime
FROM openjdk:17-jdk-slim as production

# Set a working directory inside the container
WORKDIR /app

# Copy the JAR file from the builder stage into the production image
COPY --from=builder /app/target/aline-gateway-0.0.1-SNAPSHOT.jar /app/aline-gateway.jar

# Expose the port the microservice runs on
EXPOSE 8080

# Command to run the microservice
ENTRYPOINT ["java", "-jar", "/app/aline-gateway.jar"]
