package org.example.scaffold.core.repository;

import org.assertj.core.util.Lists;
import org.example.scaffold.core.domain.User;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.test.context.ActiveProfiles;

import javax.annotation.Resource;
import java.util.ArrayList;

@DataJpaTest
@ActiveProfiles("test")
public class UserRepositoryTest {

    @Resource
    private UserRepository userRepository;

    @BeforeEach
    public void setup() {
        userRepository.deleteAll();
    }

    @Test
    public void test_user_save() {
        User admin = new User(1L, "admin");
        User savedUser = userRepository.save(admin);
        Assertions.assertEquals(admin.getId(), savedUser.getId());
        Assertions.assertEquals(admin.getName(), savedUser.getName());
    }

    @Test
    public void test_user_find_all() {
        User admin = new User(1L, "admin");
        userRepository.save(admin);
        Iterable<User> all = userRepository.findAll();
        ArrayList<User> users = Lists.newArrayList(all.iterator());
        Assertions.assertEquals(1, users.size());
        Assertions.assertEquals(1, users.get(0).getId());
        Assertions.assertEquals("admin", users.get(0).getName());
    }

}
