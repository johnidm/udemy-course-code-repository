package com.johnidouglas.ai.services;

import java.util.Map;
import java.util.concurrent.ConcurrentHashMap;

import org.springframework.stereotype.Service;

@Service
public class StockPriceService {

  private static final Map<Stock, Double> data = new ConcurrentHashMap<>();

  static {
    data.put(new Stock("Google"), 101.00);
    data.put(new Stock("Microsoft"), 100.00);

  }

  public Double getStockPrice(Stock stock) {

    System.out.println(null == stock ? "Stock is null" : "Stock is not null " + stock.name());

    return data.keySet().stream()
        .filter(s -> s.name().equalsIgnoreCase(stock.name()))
        .map(s -> data.get(s))
        .findFirst()
        .orElse(-1.0);
  }

  public record Stock(String name) {
  }
}