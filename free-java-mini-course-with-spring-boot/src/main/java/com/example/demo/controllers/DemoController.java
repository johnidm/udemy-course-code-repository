package com.example.demo.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.services.DemoService;

@RestController()
@RequestMapping("/demo")
public class DemoController {

    @Autowired
    private DemoService demoService;

    @GetMapping("")
    public String sayHi() {
        return "Hi Demo!";
    }

    @GetMapping("/all")
    public List<String> getAll() {
        return demoService.getAll();
    }

}
