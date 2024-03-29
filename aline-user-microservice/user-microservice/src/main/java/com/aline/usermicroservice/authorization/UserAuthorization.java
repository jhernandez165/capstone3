package com.aline.usermicroservice.authorization;

import com.aline.core.dto.response.UserResponse;
import com.aline.core.security.service.AbstractAuthorizationService;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.stereotype.Component;

@Component("authService")
public class UserAuthorization extends AbstractAuthorizationService<UserResponse> {
    @Override
    public boolean canAccess(UserResponse returnObject) {
        return (returnObject.getUsername().equals(getUsername()) || roleIsManagement() || roleIsAdmin());
    }

    public boolean canAccess(long userId) {
        return (getUser().getId() == userId) || roleIsManagement() || roleIsAdmin();
    }

    private boolean roleIsAdmin() {
        Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
        return authentication.getAuthorities().contains(new SimpleGrantedAuthority("ROLE_ADMIN"));
    }
}