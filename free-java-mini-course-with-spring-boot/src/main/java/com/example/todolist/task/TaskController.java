package com.example.todolist.task;
import java.time.LocalDateTime;
import java.util.UUID;
import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.todolist.utils.Utils;

import jakarta.servlet.http.HttpServletRequest;


@RestController
@RequestMapping("/tasks")
public class TaskController {
 
    @Autowired
    private ITaskRepository taskRepository;

    @SuppressWarnings("rawtypes")
    @PostMapping("/")
    public ResponseEntity create(@RequestBody TaskModel taskBody, HttpServletRequest request) {        
        LocalDateTime currentDate = LocalDateTime.now();

        if ( currentDate.isAfter(taskBody.getStartAt()) || currentDate.isEqual(taskBody.getEndAt())) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("The startAt or endAt date must be in the future");
        }

        if (taskBody.getStartAt().isAfter(taskBody.getEndAt())) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("The endAt date must be after the startAt date");
        }

        UUID userId = (UUID) request.getAttribute("userId");
        taskBody.setUserId(userId);

        TaskModel taskCreated = this.taskRepository.save(taskBody);
        return ResponseEntity.status(HttpStatus.CREATED).body(taskCreated);
    }

    @GetMapping("/all")
    public ResponseEntity<List<TaskModel>> list( HttpServletRequest request ) {
        UUID userId = (UUID) request.getAttribute("userId");

        List<TaskModel> tasks = this.taskRepository.findByUserId(userId);
        return ResponseEntity.status(HttpStatus.OK).body(tasks);
    }

    
    @PutMapping("/{id}")
    public ResponseEntity<?> update(@PathVariable UUID id, @RequestBody TaskModel taskBody,  HttpServletRequest request) {
        UUID userId = (UUID) request.getAttribute("userId");

        TaskModel task = this.taskRepository.findById(id).orElse(null);

        if (task == null) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Task not found");
        }

        if (!task.getUserId().equals(userId)) {
            return ResponseEntity.status(HttpStatus.FORBIDDEN).body("User not allowed to update this task");
        }

        Utils.copyNonNullProperties(taskBody, task);
 
        TaskModel taskUpdated = this.taskRepository.save(task);
        return ResponseEntity.status(HttpStatus.OK).body(taskUpdated);
       
    }

}