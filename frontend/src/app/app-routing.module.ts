import { ContactComponent } from './contact/contact.component';
import { inquiryRoutes } from './inquiry/inquiry.route';
import { PeopleComponent } from './people/people.component';
import { InquiryComponent } from './inquiry/inquiry.component';
import { accountRoutes } from './account/account.route';
import { homeRoutes } from './home/home.routes';
import { authsRoutes } from './auths/auths.routes';
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { messageRoutes } from './message/message.route';


const routes: Routes = [
  { path: 'auths', children: [...authsRoutes]},
  { path: 'account', children: [...accountRoutes]},
  { path: 'contact', component: ContactComponent },
  { path: 'home', children: [...homeRoutes]},
  { path: 'inquiry', children: [...inquiryRoutes] },
  { path: 'people', component: PeopleComponent },
  { path: 'message', children: [...messageRoutes] },
  { path: '', component: LandingpageComponent, pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
