package com.example.todolist.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import at.favre.lib.crypto.bcrypt.BCrypt;



@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private IUserRepository userRepository;


    @SuppressWarnings("rawtypes")
    @PostMapping("/")
    public ResponseEntity create(@RequestBody UserModel user) {
       var savedUser = this.userRepository.findByUsername(user.getUsername());
         if (savedUser != null) {
            return ResponseEntity.badRequest().body("User already exists");
        }

        var encryptedPassword = BCrypt.withDefaults().hashToString(12, user.getPassword().toCharArray());
        user.setPassword(encryptedPassword);

        UserModel userCreated = this.userRepository.save(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(userCreated);
    }

}