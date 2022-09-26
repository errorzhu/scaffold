package org.example.scaffold.base.config;


import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;


@Configuration
public class SpringDocConfig {

    @Value("${application.name:app}")
    private String applicationName;

    @Value("${swagger.enable:true}")
    private boolean enable;


    @Bean
    public OpenAPI openAPI() {
        return new OpenAPI()
                .info(new Info().title(applicationName + "API文档")
                        .description(applicationName + "API文档")
                        .version("v1.0.0"));

    }

}



