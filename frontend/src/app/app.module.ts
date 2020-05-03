import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Ng5SliderModule } from 'ng5-slider';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FooterWhiteComponent } from './shared/footer-white/footer-white.component';
import { NavbarNonAuthComponent } from './shared/navbar/navbar-non-auth/navbar-non-auth.component';
import { SignupComponent } from './auths/signup/signup.component';
import { LoginComponent } from './auths/login/login.component';
import { HomeComponent } from './home/home.component';
import { PostComponent } from './home/post/post.component';
import { AskComponent } from './home/ask/ask.component';
import { NavbarAuthComponent } from './shared/navbar/navbar-auth/navbar-auth.component';
import { SliderComponent } from './shared/slider/slider.component';
import { LikeBtnComponent } from './shared/button/like-btn/like-btn.component';
import { ReplyBtnComponent } from './shared/button/reply-btn/reply-btn.component';
import { ShareBtnComponent } from './shared/button/share-btn/share-btn.component';

@NgModule({
  declarations: [
    AppComponent,
    LandingpageComponent,
    FooterWhiteComponent,
    NavbarNonAuthComponent,
    SignupComponent,
    LoginComponent,
    HomeComponent,
    PostComponent,
    AskComponent,
    NavbarAuthComponent,
    SliderComponent,
    LikeBtnComponent,
    ReplyBtnComponent,
    ShareBtnComponent
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FontAwesomeModule,
    FormsModule,
    NgSelectModule,
    Ng5SliderModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
