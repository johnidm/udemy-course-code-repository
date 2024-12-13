package com.johnidouglas.ai.controller;

import java.util.Map;

import org.springframework.ai.chat.model.ChatModel;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chat/model")
public class ChatModelController {

    private final ChatModel chatModel;

    public ChatModelController(ChatModel chatModel) {
        this.chatModel = chatModel;

    }

    @GetMapping("")
    public Map<String, String> getGenerate(@RequestParam String input) {
        return Map.of("answer", chatModel.call(input));
    }

}