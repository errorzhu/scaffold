package org.example.microservice.userservice.controller;


import com.alibaba.csp.sentinel.annotation.SentinelResource;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.example.microservice.base.response.BaseApiResponse;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.context.config.annotation.RefreshScope;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Tag(name = "UserServiceController", description = "用户服务")
@RefreshScope
@RestController
public class UserServiceController {



    @Value("${app.user.name}")
    private String name;

    @Operation(summary = "打印接口", description = "打印接口")
    @SentinelResource(value = "echo")
    @GetMapping(value = "/echo/{string}")
    public BaseApiResponse<String> echo(@PathVariable String string) {
        return BaseApiResponse.successWithData("Hello Nacos Discovery " + string);
    }
}
