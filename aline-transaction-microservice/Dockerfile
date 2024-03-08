# Builder stage
FROM maven:3.8.1-jdk-11 as builder
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests

# Final stage
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=builder /app/transaction-microservice/target/transaction-microservice-0.1.0.jar /app/transaction-microservice.jar

# Expose the port the application runs on
EXPOSE 8072

# Run the JAR file
ENTRYPOINT ["java", "-jar", "/app/transaction-microservice.jar"]
