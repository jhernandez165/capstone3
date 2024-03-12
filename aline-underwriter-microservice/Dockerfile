# Stage 1: Build the application
FROM maven:3.9.6-eclipse-temurin-17 as builder
WORKDIR /app

# Copy the source code
COPY . .

# Build the application without running tests
RUN mvn clean package -DskipTests

# Stage 2: Create the runtime image
FROM openjdk:11-jre-slim as production
WORKDIR /app

# Copy the JAR file from the builder stage
COPY --from=builder /app/underwriter-microservice/target/underwriter-microservice-0.1.0.jar /app/underwriter-microservice.jar

# Expose the port the application runs on
EXPOSE 8071

# Run the JAR file
ENTRYPOINT ["java", "-jar", "/app/underwriter-microservice.jar"]
