package com.johnidouglas.ai.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.reactive.function.client.WebClient;
import reactor.core.publisher.Mono;

@RestController
@RequestMapping("/chat/client/request")
public class ChatClientRequestController {

    private final WebClient webClient;

    @Value("${spring.ai.openai.api-key}")
    private String OPENAI_API_KEY;

    @Value("${spring.ai.openai.chat.options.model}")
    private String OPENAI_API_MODEL;

    private static final String OPENAI_API_URL = "https://api.openai.com/v1";

    public ChatClientRequestController(WebClient.Builder webClientBuilder) {
        this.webClient = webClientBuilder
                .baseUrl(OPENAI_API_URL)
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();
    }

    @GetMapping("")
    public Mono<String> chat(@RequestParam String input) {

        return webClient.post()
                .uri("/chat/completions")
                .header(HttpHeaders.AUTHORIZATION, "Bearer " + OPENAI_API_KEY)
                .bodyValue(Map.of(
                        "model", OPENAI_API_MODEL,
                        "messages", List.of(Map.of("role", "user", "content", input))))
                .retrieve()
                .bodyToMono(String.class);
    }
}