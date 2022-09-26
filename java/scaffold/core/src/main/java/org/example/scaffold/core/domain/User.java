package org.example.scaffold.core.domain;


import javax.persistence.*;


@Entity
@Table(name = "user")
public class User {
    @Id
    @Column(name = "ID")
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    @Column(name = "NAME")
    private String name;


    public Long getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
