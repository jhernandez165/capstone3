import { Injectable } from '@angular/core';
import jwtDecode from 'jwt-decode';
import { JWT } from '@core/models/jwt.model';

@Injectable({
  providedIn: 'root'
})
export class JwtService {

  constructor() { }

  saveJwt(token: string): void {
    console.log('Saving JWT to storage:', token);
    // Correctly format the token to ensure 'Bearer ' prefix is handled properly
    const formattedToken = token.startsWith('Bearer ') ? token.substring(7) : token;
    localStorage.setItem('jwt', formattedToken);
    console.log('JWT after saving:', localStorage.getItem('jwt'));
  }

  deleteJwt(): void {
    localStorage.removeItem('jwt');
  }

  getJwt(): string | null {
    return localStorage.getItem('jwt');
  }

  parseJwt(): JWT | null {
    try {
      const token = this.getJwt();
      return token ? jwtDecode<JWT>(token) : null;
    } catch (error) {
      console.error('Error decoding token:', error);
      return null;
    }
  }

  getUsername(): string | null {
    return this.parseJwt()?.sub ?? null;
  }

  getRole(): string | null {
    return this.parseJwt()?.authority ?? null;
  }

  getIssueAtDate(): Date | null {
    const iat = this.parseJwt()?.iat;
    return iat ? new Date(iat * 1000) : null;
  }

  getExpirationDate(): Date | null {
    const exp = this.parseJwt()?.exp;
    return exp ? new Date(exp * 1000) : null;
  }

  isValid(): boolean {
    const now = new Date();
    const expirationDate = this.getExpirationDate();
    return expirationDate ? expirationDate.getTime() > now.getTime() : false;
  }
}
