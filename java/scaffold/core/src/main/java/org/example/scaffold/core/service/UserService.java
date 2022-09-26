package org.example.scaffold.core.service;


import com.google.common.collect.Streams;
import org.example.scaffold.core.repository.UserRepository;
import org.example.scaffold.core.vo.UserVO;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.List;
import java.util.stream.Collectors;

@Service
public class UserService {

    @Resource
    private UserRepository userRepository;

    public List<UserVO> findAll() {



        return Streams.stream(userRepository.findAll())
                .map(x -> new UserVO(x.getId(), x.getName()))
                .collect(Collectors.toList());

    }

}
