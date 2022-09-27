package org.example.scaffold.core.controller;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.collect.ImmutableList;
import org.example.scaffold.base.response.BaseApiResponse;
import org.example.scaffold.core.service.UserService;
import org.example.scaffold.core.vo.UserVO;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

import javax.annotation.Resource;
import java.nio.charset.StandardCharsets;
import java.util.List;


@SpringBootTest
@AutoConfigureMockMvc
public class UserControllerTest {

    @Resource
    MockMvc mockMvc;

    @Resource
    ObjectMapper om;

    @MockBean
    UserService userService;

    @Resource
    UserController userController;
    
    @Test
    public void test_user_controller_find_all() throws Exception {

        Mockito.when(userService.findAll()).thenReturn(ImmutableList.of(new UserVO(1L,"admin")));
        MvcResult mvcResult = mockMvc.perform(MockMvcRequestBuilders.get("/demo/api/v1/users")
                        .contentType(MediaType.APPLICATION_JSON)
                ).andExpect(MockMvcResultMatchers.status().isOk())
                .andExpect(MockMvcResultMatchers.jsonPath("$.code").value("0"))
                .andExpect(MockMvcResultMatchers.jsonPath("$.data[0].id").value("1"))
                .andExpect(MockMvcResultMatchers.jsonPath("$.data[0].name").value("admin"))
                .andReturn();
        String contentAsString = mvcResult.getResponse().getContentAsString(StandardCharsets.UTF_8);
        BaseApiResponse<List<UserVO>> response = om.readValue(contentAsString, new TypeReference<BaseApiResponse<List<UserVO>>>() {
        });
        Assertions.assertEquals(0,response.getCode());
        Assertions.assertEquals("成功",response.getMsg());
        Assertions.assertEquals(1,response.getData().size());
        Assertions.assertEquals("admin",response.getData().get(0).getName());
        Assertions.assertEquals(1,response.getData().get(0).getId());

    }
}
