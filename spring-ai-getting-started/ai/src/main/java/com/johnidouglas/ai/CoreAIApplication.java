package com.johnidouglas.ai;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CoreAIApplication {

	public static void main(String[] args) {
		SpringApplication.run(CoreAIApplication.class, args);
		System.out.println("Spring AI Chat Application Started...");
	}

}
