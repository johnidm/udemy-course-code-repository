package com.example.demo.services;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;

@Service
public class DemoService {

    public List<String> getAll() {
        return new ArrayList<String>() {
            {
                add("Demo 1");
                add("Demo 2");
                add("Demo 3");
            }
        };
    }
}