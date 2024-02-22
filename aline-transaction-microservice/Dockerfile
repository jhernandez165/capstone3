# Use Maven for building the application
FROM maven:3.9.6-eclipse-temurin-17 as builder
WORKDIR /app
COPY . .
RUN mvn clean package -DskipTests
# Copy the built JAR file from the build stage
COPY --from=build /app/target/*.jar ./transaction-microservice-0.1.0.jar
# Expose port 8080
EXPOSE 8072
# Command to run the application
CMD ["java", "-jar", "transaction-microservice-0.1.0.jar"]
