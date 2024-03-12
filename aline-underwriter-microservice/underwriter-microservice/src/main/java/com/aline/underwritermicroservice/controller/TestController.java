package com.aline.underwritermicroservice.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@Slf4j
@RestController
public class TestController {

    @GetMapping("/test/log")
    public String testLog() {
        log.info("Test logging endpoint was called.");
        return "Logging test successful!";
    }
}
