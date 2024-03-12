import React, { createContext, useContext, useEffect, useState } from 'react';
import jwt_decode from 'jwt-decode';
import PropTypes from 'prop-types';

export const UserSessionContext = createContext({
    authorities: {},
    logoutMethod: () => {},
    loggedIn: false,
    token: '',
    expired: true,
    user: ''
});

export const UpdateUserSessionContext = createContext({
    updateUser: () => {}
});

export function UseUserSession() {
    const { authority, logoutMethod, loggedIn, token, expired, user } = useContext(UserSessionContext);
    return { authority, logoutMethod, loggedIn, token, expired, user };
}

export function UpdateUserSession() {
    const { updateUser } = useContext(UpdateUserSessionContext);
    return { updateUser };
}

export default function UserSessionProvider({ children }) {
    const STORAGE_NAME = process.env.REACT_APP_TOKEN_NAME;
    const [token, setToken] = useState(userTokenInitialState);

    const fetchTokenFromStorage = () => {
        let fullToken = localStorage.getItem(STORAGE_NAME);
        if (fullToken && fullToken.startsWith('Bearer ')) {
            try {
                const decodedJWT = jwt_decode(fullToken.replace('Bearer ', ''));
                const isExpired = Date.now() >= decodedJWT.exp * 1000;
                if (isExpired) {
                    localStorage.removeItem(STORAGE_NAME);
                }
                const isLoggedIn = !isExpired && decodedJWT.authority === 'administrator';

                setToken({
                    jwt: fullToken,
                    authority: decodedJWT.authority,
                    expired: isExpired,
                    loggedIn: isLoggedIn,
                    user: decodedJWT.sub
                });
            } catch (e) {
                console.error('Error decoding token:', e);
                setToken({ ...userTokenInitialState, checkedStorage: true });
            }
        } else {
            console.log('Token is either missing or does not have the correct prefix.');
            setToken({ ...userTokenInitialState });
        }
    };

    useEffect(() => {
        console.log('Checking token from storage...');
        fetchTokenFromStorage();
    }, []);

    const logout = () => {
        localStorage.removeItem(STORAGE_NAME);
        setToken(userTokenInitialState);
    };

    return (
        <UserSessionContext.Provider value={{ ...token, logoutMethod: logout }}>
            <UpdateUserSessionContext.Provider value={{ updateUser: fetchTokenFromStorage }}>
                {children}
            </UpdateUserSessionContext.Provider>
        </UserSessionContext.Provider>
    );
}

UserSessionProvider.propTypes = {
    children: PropTypes.element
};

const userTokenInitialState = {
    jwt: '',
    authority: {},
    loggedIn: false,
    expired: true,
    user: '',
    checkedStorage: false // Ensures token check from storage is attempted at least once
};
