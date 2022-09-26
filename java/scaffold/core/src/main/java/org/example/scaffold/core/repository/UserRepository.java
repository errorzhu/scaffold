package org.example.scaffold.core.repository;

import org.example.scaffold.core.domain.User;
import org.springframework.data.repository.CrudRepository;

public interface UserRepository extends CrudRepository<User,Long> {
}
