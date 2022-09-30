package org.example.microservice.userservice;


import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.ConfigurableApplicationContext;

@SpringBootApplication(scanBasePackages = { "org.example.microservice" })
@EnableDiscoveryClient
public class UserServiceApplication {
    public static void main(String[] args) {
        ConfigurableApplicationContext configurableApplicationContext = SpringApplication.run(UserServiceApplication.class, args);
        System.out.println(configurableApplicationContext.getEnvironment().getProperty("app.user.name"));
    }
}
