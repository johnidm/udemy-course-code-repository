package com.johnidouglas.ai.config;

import java.util.function.Function;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Description;

import com.johnidouglas.ai.services.MockWeatherService;
import com.johnidouglas.ai.services.RectangleAreaService;
import com.johnidouglas.ai.services.StockPriceService;
import com.johnidouglas.ai.services.StockPriceService.Stock;

@Configuration
public class Functions {

    @Bean
    @Description("Calculate the area of a rectangle from its base and height")
    public Function<RectangleAreaService.Request, RectangleAreaService.Response> rectangeleAreaFunction() {
        return new RectangleAreaService();
    }

    @Bean
    @Description("Get the weather in location")
    public Function<MockWeatherService.Request, MockWeatherService.Response> weatherFunction() {
        return new MockWeatherService();
    }

    @Bean
    @Description("Get price by stock name")
    public Function<Stock, Double> priceByStockNameFunction(StockPriceService stockPriceService) {
      return stockPriceService::getStockPrice;
    }

}