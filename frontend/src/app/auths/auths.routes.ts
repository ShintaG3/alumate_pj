import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { Routes } from '@angular/router';

export const authsRoutes: Routes = [
  { path: 'signup', component: SignupComponent },
  { path: 'login', component: LoginComponent },
];
