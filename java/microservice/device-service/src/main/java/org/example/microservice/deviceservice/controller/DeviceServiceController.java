package org.example.microservice.deviceservice.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.example.microservice.base.response.BaseApiResponse;
import org.springframework.cloud.client.ServiceInstance;
import org.springframework.cloud.client.loadbalancer.LoadBalancerClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

import javax.annotation.Resource;
import java.net.MalformedURLException;

@Tag(name = "DeviceServiceController", description = "设备服务")
@RestController
public class DeviceServiceController {

    @Resource
    private LoadBalancerClient loadBalancerClient;

    @Resource
    private RestTemplate restTemplate;

    @Operation(summary = "调用服务发现的接口",description = "调用服务发现的接口")
    @GetMapping("/echo/app-name")
    public BaseApiResponse<String> echoAppName(@RequestParam String appName) throws MalformedURLException {
        ServiceInstance serviceInstance = loadBalancerClient.choose("user-service");
        System.out.println(serviceInstance.getUri().toURL().toString());
        String url = String.format("http://%s:%s/echo/%s", serviceInstance.getHost(), serviceInstance.getPort(), appName);
        return BaseApiResponse.successWithData(restTemplate.getForObject(url, String.class));
    }

}

