import { MessageComponent } from './message/message.component';
import { PeopleComponent } from './people/people.component';
import { InquiryComponent } from './inquiry/inquiry.component';
import { accountRoutes } from './account/account.route';
import { homeRoutes } from './home/home.routes';
import { authsRoutes } from './auths/auths.routes';
import { SignupComponent } from './auths/signup/signup.component';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingpageComponent } from './landingpage/landingpage.component';


const routes: Routes = [
  { path: 'auths', children: [...authsRoutes]},
  { path: 'account', children: [...accountRoutes]},
  { path: 'home', children: [...homeRoutes]},
  { path: 'inquiry', component: InquiryComponent },
  { path: 'people', component: PeopleComponent },
  { path: 'message', component: MessageComponent },
  { path: '', component: LandingpageComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
