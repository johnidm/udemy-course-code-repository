package com.johnidouglas.ai.controller;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.core.io.Resource;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;

import java.util.Map;

@RestController
public class HomeController {

    @Value("classpath:/prompts/youtube.st")
    private Resource promptYouTube;

    @Value("${spring.ai.openai.chat.options.model}")
    private String openAiModel;

    @GetMapping("/")
    public String getHome() {
        return "API is running";
    }

    @GetMapping("/template/youtube")
    public String getTYTemplate() throws IOException {
        return new String(promptYouTube.getInputStream().readAllBytes(), StandardCharsets.UTF_8);
    }

    @GetMapping("/openai")
    public Map<String, String> getOpenAI() {
        return Map.<String, String>of("model", openAiModel);
    }

}
