package org.example.scaffold.core.service;

import com.google.common.collect.ImmutableList;
import org.example.scaffold.core.domain.User;
import org.example.scaffold.core.repository.UserRepository;
import org.example.scaffold.core.vo.UserVO;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;

import javax.annotation.Resource;
import java.util.List;

@SpringBootTest
public class UserServiceTest {

    @Resource
    UserService userService;

    @MockBean
    UserRepository userRepository;


    @Test
    public void test_user_service_find_all() {

        User admin = new User(1L, "admin");
        Mockito.when(userRepository.findAll()).thenReturn(ImmutableList.of(admin));
        List<UserVO> all = userService.findAll();
        Assertions.assertEquals(1,all.size());
        Assertions.assertEquals(1,all.get(0).getId());
        Assertions.assertEquals("admin",all.get(0).getName());

    }
}
