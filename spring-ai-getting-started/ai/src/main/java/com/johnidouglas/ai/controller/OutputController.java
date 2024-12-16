package com.johnidouglas.ai.controller;

import java.util.List;
import java.util.Map;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatModel;
import org.springframework.ai.converter.ListOutputConverter;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.core.convert.support.DefaultConversionService;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/chat/output")
public class OutputController {

    record ActorsFilms(String actor, List<String> movies) {
    }

    private final ChatModel chatModel;

    public OutputController(ChatModel chatModel) {
        this.chatModel = chatModel;
    }

    @RequestMapping("/map")
    public Map<String, Object> getMap() {
        Map<String, Object> result = ChatClient.create(chatModel).prompt()
                .user(u -> u.text("Provide me a List of {subject}")
                        .param("subject", "an array of numbers from 1 to 9 under they key name 'numbers'"))
                .call()
                .entity(new ParameterizedTypeReference<Map<String, Object>>() {
                });

        return result;
    }

    @RequestMapping("/bean")
    public List<ActorsFilms> getBean() {
        return ChatClient.create(chatModel).prompt()
                .user("Generate the filmography of 5 movies for Tom Hanks and Bill Murray.")
                .call()
                .entity(new ParameterizedTypeReference<List<ActorsFilms>>() {
                });
    }

    @RequestMapping("/list")
    public List<String> getList() {
        return ChatClient.create(chatModel).prompt()
                .user(u -> u.text("List five {subject}")
                        .param("subject", "ice cream flavors"))
                .call()
                .entity(new ListOutputConverter(new DefaultConversionService()));
    }

}