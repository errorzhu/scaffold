package org.example.scaffold.core.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.example.scaffold.base.response.BaseApiResponse;
import org.example.scaffold.core.service.UserService;
import org.example.scaffold.core.vo.UserVO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.List;

@Tag(name = "UserController", description = "用户管理")
@RestController
@RequestMapping("/demo/api/v1")
public class UserController {


    @Resource
    private UserService userService;

    @Operation(summary = "获取用户",description = "获取用户")
    @GetMapping
    public BaseApiResponse<List<UserVO>> findAll() {
        return BaseApiResponse.successWithData(userService.findAll());
    }

}
