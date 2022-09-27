package org.example.scaffold.core.domain;


import org.hibernate.annotations.GenericGenerator;

import javax.persistence.*;


@Entity
@Table(name = "user")
public class User {
    @Id
    @Column(name = "ID")
    @GeneratedValue(strategy = GenerationType.AUTO,generator = "myid")
    @GenericGenerator(name="myid",strategy = "org.example.scaffold.core.utils.CustomIdGenerator")
    private Long id;

    public User() {
    }

    public User(Long id, String name) {
        this.id = id;
        this.name = name;
    }

    @Column(name = "NAME")
    private String name;


    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
