package com.example.todolist.filter;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.FilterChain;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Base64;
import java.util.List;

import jakarta.servlet.ServletException;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import com.example.todolist.user.IUserRepository;
import com.example.todolist.user.UserModel;

import at.favre.lib.crypto.bcrypt.BCrypt;

@Component
public class FilterTaskAuth extends OncePerRequestFilter {

    @Autowired
    private IUserRepository userRepository;

    @SuppressWarnings("null")
    @Override
    protected void doFilterInternal(@SuppressWarnings("null") HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws IOException, ServletException {
        
        List<String> allowedPath = new ArrayList<>() {
            {
                add("/users/");
                add("/h2-console");
            }
        };

        String path = request.getServletPath();

        if (allowedPath.stream().anyMatch(path::startsWith)) {
            filterChain.doFilter(request, response);
            return;
        }
        
        String token = request.getHeader("Authorization");
        if (token == null || !token.startsWith("Basic")) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Missing token");
            return;
        }

        String authEncoded = token.substring("Bearer".length()).trim();
        byte[] authDecoded = Base64.getDecoder().decode(authEncoded);

        String auth = new String(authDecoded);
        String[] credential = auth.split(":");

        String userName = credential[0];
        String password = credential[1];

        UserModel user = userRepository.findByUsername(userName);
        if (user == null) {
            response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "User not found");            
        } else {
            Boolean isPasswordMatch = BCrypt.verifyer().verify(password.toCharArray(), user.getPassword().toCharArray()).verified;
            if (!isPasswordMatch) {
                response.sendError(HttpServletResponse.SC_UNAUTHORIZED, "Password not match");
            } else {
                request.setAttribute("userId", user.getId());
                filterChain.doFilter(request, response);
            }
        }
    }
}