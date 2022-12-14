package org.example.scaffold.core.vo;

public class UserVO {

    private Long id;
    private String name;

    public UserVO(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
