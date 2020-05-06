import { BaseConnectComponent } from './base-connect/base-connect.component';
import { BaseInquiryComponent } from './base-inquiry/base-inquiry.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { Routes } from '@angular/router';

export const authsRoutes: Routes = [
  { path: 'base-inquiry', component: BaseInquiryComponent },
  { path: 'base-connect', component: BaseConnectComponent },
  { path: 'signup', component: SignupComponent },
  { path: 'login', component: LoginComponent },
];
