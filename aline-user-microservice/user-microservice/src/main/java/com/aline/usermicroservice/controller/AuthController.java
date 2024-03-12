package com.aline.usermicroservice.controller;
import org.springframework.http.HttpHeaders;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AuthController {

    @Autowired
    private AuthenticationManager authenticationManager;

    @PostMapping("/login")
    public ResponseEntity<?> authenticateUser(@RequestBody LoginRequest loginRequest) {
        Authentication authentication = authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(
                        loginRequest.getUsername(),
                        loginRequest.getPassword()
                )
        );
        String jwt = generateJwtToken(authentication);
    
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", "Bearer " + jwt);
        return ResponseEntity.ok().headers(headers).body(new JwtResponse(jwt));
    }

    // Placeholder method for generating a JWT token
    private String generateJwtToken(Authentication authentication) {
        // Implement JWT token generation logic here
        return "token";
    }

    // Inner class for login request
    static class LoginRequest {
        private String username;
        private String password;
    
        // Getter for username
        public String getUsername() {
            return username;
        }
    
        // Setter for username
        public void setUsername(String username) {
            this.username = username;
        }
    
        // Getter for password
        public String getPassword() {
            return password;
        }
    
        // Setter for password
        public void setPassword(String password) {
            this.password = password;
        }
    }

    // Inner class for JWT response
    static class JwtResponse {
        private String token;

        public JwtResponse(String token) {
            this.token = token;
        }

        // Getter for token
        public String getToken() {
            return token;
        }
    }
}