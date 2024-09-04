package com.example.absensi.controller;

import com.example.absensi.model.Absensi;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Map;

@Controller
public class AbsensiController {
    private final RestTemplate restTemplate;

    public AbsensiController(RestTemplate restTemplate) {
        this.restTemplate = restTemplate;
    }

    @GetMapping("/absensi")
    public String getAbsensi(Model model) {
        String url = "http://127.0.0.1:5000/absensi";
        List<Map<String, Object>> absensiList = restTemplate.getForObject(url, List.class);
        model.addAttribute("absensiList", absensiList);
        model.addAttribute("absensi", new Absensi()); // Untuk inisialisasi objek Absensi kosong
        return "absensi";
    }

    @PostMapping("/addAbsensi")
    public String addAbsensi(Absensi absensi) {
        String url = "http://127.0.0.1:5000/absensi";
        restTemplate.postForObject(url, absensi, Void.class); // Mengirimkan objek absensi ke endpoint POST
        return "redirect:/absensi";
    }
}
