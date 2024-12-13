package com.johnidouglas.ai.controller;

import java.util.List;
import java.util.Map;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.converter.ListOutputConverter;
import org.springframework.ai.converter.MapOutputConverter;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.convert.support.DefaultConversionService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.johnidouglas.ai.DTO.ChatInput;

@RestController
@RequestMapping("/chat/prompt")
public class PromtpController {

    private final ChatClient chatClient;

    public PromtpController(ChatClient.Builder builder) {
        this.chatClient = builder.build();
    }

    @SuppressWarnings("null")
    @GetMapping("/songs")
    public List<String> getSongsByArtist(@RequestParam(value = "artist", defaultValue = "Taylor Swift") String artist) {
        var message = """
                Please give me a list of top 10 songs for the artist {artist}. If you don't know the answer, just say

                {format}
                """;

        ListOutputConverter out = new ListOutputConverter(new DefaultConversionService());

        PromptTemplate promptTemplate = new PromptTemplate(
                message, Map.of("artist", artist,
                        "format", out.getFormat()));

        Prompt prompt = new Prompt(promptTemplate.createMessage());
        String content = chatClient.prompt(prompt).call().content();
        return out.convert(content);
    }

    @SuppressWarnings("null")
    @GetMapping("/author/{author}")
    public Map<String, Object> getAuthorsSocialLinks(@PathVariable String author) {
        String promptMessage = """
                Generate a list of links for the author {author}. Include the author's name as the key and any social network links

                {format}.
                """;

        MapOutputConverter out = new MapOutputConverter();
        String format = out.getFormat();

        PromptTemplate promptTemplate = new PromptTemplate(promptMessage, Map.of("author", author, "format", format));
        Prompt prompt = new Prompt(promptTemplate.createMessage());
        String content = chatClient.prompt(prompt).call().content();
        return out.convert(content);

    }


}