package org.example.scaffold.core.domain;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class UserTest {


    @Test
    public void test_user_created() {
        User user = new User(1L,"admin");
        Assertions.assertEquals(user.getId(), 1);
        Assertions.assertEquals(user.getName(), "admin");
    }

}
