package com.johnidouglas.ai.controller;

import java.util.Map;

import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.model.Generation;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.openai.OpenAiChatOptions;
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

    @GetMapping("/function")
    public Generation getPrompt(@RequestParam String input) {

        Prompt prompt = new Prompt(input, OpenAiChatOptions
                .builder()
                .withFunction("rectangeleAreaFunction")
                .withFunction("weatherFunction")
                .withFunction("priceByStockNameFunction")
                .build());

        ChatResponse response = chatModel.call(prompt);

        return response.getResult();
    }

}

// ChatRequest request = new ChatRequest();
// request.setMessage(userInput);
// ChatResponse response = chatClient.sendMessage(request);
// return response.getReply();