package com.sme.climatedata.controller;

//rest controller class for climate details for CRUD operation
import com.sme.climatedata.model.ClimateData;
import com.sme.climatedata.service.ClimateService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/climate")
public class ClimateController {
    private final ClimateService climateService;

    @Autowired
    public ClimateController(ClimateService climateService) {
        this.climateService = climateService;
    }

    @GetMapping
    public List<ClimateData> getAllClimateData() {
        return climateService.getAllClimateData();
    }

    @GetMapping("/{id}")
    public ClimateData getClimateDataById(@PathVariable Long id) {
        return climateService.getClimateDataById(id);
    }

    @PostMapping
    public ClimateData createClimateData(@RequestBody ClimateData climateData) {
        return climateService.createClimateData(climateData);
    }

    @PutMapping("/{id}")
    public ClimateData updateClimateData(@PathVariable Long id, @RequestBody ClimateData climateData) {
        return climateService.updateClimateData(id, climateData);
    }

    @DeleteMapping("/{id}")
    public void deleteClimateData(@PathVariable Long id) {
        climateService.deleteClimateData(id);
    }

    @GetMapping("/city")
    public List<ClimateData> getClimateDataByCity() {
        return climateService.getClimateDataByCity();
    }
}