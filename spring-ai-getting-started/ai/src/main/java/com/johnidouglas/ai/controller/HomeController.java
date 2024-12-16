package com.johnidouglas.ai.controller;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.core.io.Resource;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

import java.util.Map;

@RestController
public class HomeController {

    @Value("${spring.ai.openai.chat.options.model}")
    private String openAiModel;

    @GetMapping("/")
    public String getHome() {
        return "API is running";
    }

   

    @GetMapping("/openai")
    public Map<String, String> getOpenAI() {
        return Map.<String, String>of("model", openAiModel);
    }

}
