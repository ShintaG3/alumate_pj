import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FooterWhiteComponent } from './shared/footer-white/footer-white.component';
import { NavbarNonAuthComponent } from './shared/navbar-non-auth/navbar-non-auth.component';
import { SignupComponent } from './auths/signup/signup.component';

@NgModule({
  declarations: [
    AppComponent,
    LandingpageComponent,
    FooterWhiteComponent,
    NavbarNonAuthComponent,
    SignupComponent
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FontAwesomeModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
