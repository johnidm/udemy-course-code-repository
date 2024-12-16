package com.johnidouglas.ai.controller;

import java.util.List;
import java.util.stream.Collectors;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.advisor.SimpleLoggerAdvisor;
import org.springframework.ai.converter.BeanOutputConverter;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.johnidouglas.ai.DTO.ChatInput;

import reactor.core.publisher.Flux;

@RestController
@RequestMapping("/chat/client")
public class ChatClientController {

    private final ChatClient chatClient;

    record ActorFilms(String actor, List<String> movies) {
    }

    public ChatClientController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    @GetMapping("/call")
    public String getChatCall(@RequestParam String input) {
        return chatClient.prompt()
                .system("You are a friendly chat bot that tell jokes")
                .advisors(new SimpleLoggerAdvisor())
                .user(input)

                .call()
                .content();
    }

    @GetMapping("/stream")
    public Flux<String> getChatStream(@RequestParam String input) {
        return chatClient.prompt().user(input).stream().content();

    }

    @PostMapping("")
    public String postChat(@RequestBody ChatInput input) {
        return chatClient.prompt().user(input.getInput()).call().content();
    }

    @GetMapping("/actor")
    public ActorFilms getActorFilms() {
        ActorFilms actorFilms = this.chatClient.prompt()
                .system("You are a friendly chat bot that generates filmography for actors.")
                .user("Generate the filmography for a random actor.")
                .advisors(new SimpleLoggerAdvisor())
                .call()
                .entity(ActorFilms.class);

        return actorFilms;
    }

    @GetMapping("/actors")
    public List<ActorFilms> getActorsFilms() {
        List<ActorFilms> actorsFilms = this.chatClient.prompt()
                .user("Generate the filmography of 5 movies for Tom Hanks and Bill Murray.")
                .call()
                .entity(new ParameterizedTypeReference<List<ActorFilms>>() {
                });

        return actorsFilms;
    }

    @GetMapping("/actors/stream")
    public List<ActorFilms> getActorsFilmsStream() {

        var converter = new BeanOutputConverter<>(new ParameterizedTypeReference<List<ActorFilms>>() {
        });

        Flux<String> flux = this.chatClient.prompt()
                .advisors(new SimpleLoggerAdvisor())
                .user(u -> u.text("""
                            Generate the filmography for a random actor.
                            {format}
                        """)
                        .param("format", converter.getFormat()))
                .stream()
                .content();

        String content = flux.collectList().block().stream().collect(Collectors.joining());

        List<ActorFilms> actorFilms = converter.convert(content);

        return actorFilms;
    }

}