# Stage 1: Build the application
FROM maven:3.8.7-openjdk-18 AS build

# Set the working directory
WORKDIR /app

# Copy the pom.xml and download dependencies
COPY pom.xml .
RUN mvn dependency:go-offline -B

# Copy the source code and build the application
COPY src ./src
RUN mvn clean install -Dmaven.test.skip=true

# Stage 2: Run the application
FROM openjdk:18-jdk-slim

# Set the working directory
WORKDIR /app
EXPOSE 8888
# Copy the built jar from the previous stage
COPY --from=build /app/target/*.jar app.jar

# Expose the application port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java", "-jar", "app.jar"]