package com.aline.underwritermicroservice;

import org.springframework.boot.autoconfigure.SpringBootApplication;
import com.aline.core.annotation.EnableCoreModule;
import io.swagger.v3.oas.annotations.OpenAPIDefinition;
import io.swagger.v3.oas.annotations.enums.SecuritySchemeType;
import io.swagger.v3.oas.annotations.info.Info;
import io.swagger.v3.oas.annotations.security.SecurityScheme;

import org.springframework.boot.SpringApplication;

@SpringBootApplication
@EnableCoreModule
@OpenAPIDefinition(info = @Info(
    title = "Underwriter Microservice API",
    description = "This API provides operations to either accept or deny an application for an account as well as Applicant and Member creation and management.",
    version = "1.0"
))
@SecurityScheme(
    name = "bearerAuth", // Can be set to any value
    type = SecuritySchemeType.HTTP,
    scheme = "bearer",
    bearerFormat = "JWT"
)
public class UnderwriterMicroserviceApplication {

    public static void main(String[] args) {
        SpringApplication.run(UnderwriterMicroserviceApplication.class, args);
    }

}
