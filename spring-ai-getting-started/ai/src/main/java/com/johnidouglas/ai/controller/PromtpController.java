package com.johnidouglas.ai.controller;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Map;

import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.model.ChatResponse;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.converter.BeanOutputConverter;
import org.springframework.ai.converter.ListOutputConverter;
import org.springframework.ai.converter.MapOutputConverter;
import org.springframework.ai.openai.OpenAiChatOptions;
import org.springframework.ai.openai.api.OpenAiApi.ChatModel;
import org.springframework.ai.openai.api.ResponseFormat;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.convert.support.DefaultConversionService;
import org.springframework.core.io.Resource;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.annotation.JsonProperty;

@RestController
@RequestMapping("/chat/prompt")
public class PromtpController {

    @Value("classpath:/prompts/youtube.st")
    private Resource promptYouTube;

    record MathReasoning(
            @JsonProperty(required = true, value = "steps") Steps steps,
            @JsonProperty(required = true, value = "final_answer") String finalAnswer) {

        record Steps(
                @JsonProperty(required = true, value = "items") Items[] items) {

            record Items(
                    @JsonProperty(required = true, value = "explanation") String explanation,
                    @JsonProperty(required = true, value = "output") String output) {
            }
        }
    }

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

    @SuppressWarnings("null")
    @GetMapping("/pirates/five")
    public String getChatCallResponse() {

        Prompt prompt = new Prompt(
                "Generate the names of 5 famous pirates.",
                OpenAiChatOptions.builder()
                        .withModel("gpt-4o")
                        .withTemperature(0.4)
                        .build());

        ChatResponse response = this.chatClient.prompt(prompt).call().chatResponse();

        return response.getResult().getOutput().getContent();

    }

    @SuppressWarnings("null")
    @GetMapping("/math/resolve")
    public String getMathResolveResponse() {

        String jsonSchema = """
                {
                    "type": "object",
                    "properties": {
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "explanation": { "type": "string" },
                                    "output": { "type": "string" }
                                },
                                "required": ["explanation", "output"],
                                "additionalProperties": false
                            }
                        },
                        "final_answer": { "type": "string" }
                    },
                    "required": ["steps", "final_answer"],
                    "additionalProperties": false
                }
                """;

        Prompt prompt = new Prompt("how can I solve 8x + 7 = -23",
                OpenAiChatOptions.builder()
                        .withModel(ChatModel.GPT_4_O_MINI)
                        .withResponseFormat(new ResponseFormat(ResponseFormat.Type.JSON_SCHEMA, jsonSchema))
                        .build());

        ChatResponse response = this.chatClient.prompt(prompt).call().chatResponse();

        return response.getResult().getOutput().getContent();

    }

    @SuppressWarnings("null")
    @GetMapping("/math/resolve/json")
    public MathReasoning getMathResolveResponseJson() {

        var outputConverter = new BeanOutputConverter<>(MathReasoning.class);

        var jsonSchema = outputConverter.getJsonSchema();

        Prompt prompt = new Prompt("how can I solve 8x + 7 = -23",
                OpenAiChatOptions.builder()
                        .withModel(ChatModel.GPT_4_O_MINI)
                        .withResponseFormat(new ResponseFormat(ResponseFormat.Type.JSON_SCHEMA, jsonSchema))
                        .build());

        ChatResponse response = this.chatClient.prompt(prompt).call().chatResponse();
        String content = response.getResult().getOutput().getContent();

        MathReasoning mathReasoning = outputConverter.convert(content);
        return mathReasoning;

    }

    @GetMapping("/soccer-player")
    public String getSoccer() {
        Prompt prompt = new Prompt("""
                    List the 5 best football players in the world and their personal informations.

                    The result shoud be a JSON object with the following format. Don't any other information.:
                    {
                        "players": [
                            {
                                "name": "Lionel Messi",
                                "age": 34,
                                "nacionality": "Argentina",
                            }
                        ]
                    }
                """);

        String content = chatClient.prompt(prompt).call().content();
        return content;

    }

    @GetMapping("/youtube")
    public String getTYTemplate() throws IOException {

        // return new String(promptYouTube.getInputStream().readAllBytes(), StandardCharsets.UTF_8);

        PromptTemplate promptTemplate = new PromptTemplate(promptYouTube);

        
        Prompt prompt = promptTemplate.create(Map.of("subject", "Python for begginer"));

        ChatResponse response = this.chatClient.prompt(prompt).call().chatResponse();

        return response.getResult().getOutput().getContent();

    }

}