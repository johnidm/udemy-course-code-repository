package com.johnidouglas.ai.controller;

import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.openai.OpenAiChatModel;
import org.springframework.ai.openai.OpenAiChatOptions;
import org.springframework.ai.openai.api.OpenAiApi;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chat/manual")
public class ManualClientController {

    @Value("${spring.ai.openai.api-key}")
    private String OPENAI_API_KEY;


    @GetMapping("")
    public String getAstronautsNames() {

        OpenAiApi openAiApi = new OpenAiApi(OPENAI_API_KEY);
        OpenAiChatOptions openAiChatOptions = OpenAiChatOptions.builder()
                    .withModel("gpt-3.5-turbo")
                    .withTemperature(0.4)
                    .withMaxTokens(200)
                    .build();


        OpenAiChatModel chatModel = new OpenAiChatModel(openAiApi, openAiChatOptions);

        ChatResponse response = chatModel.call(
            new Prompt("Generate the names of 5 famous astronauts."));

        return response.getResult().getOutput().getContent();
       
    }

}