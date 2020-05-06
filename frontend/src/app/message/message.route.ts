import { MessageDetailComponent } from './message-detail/message-detail.component';
import { MessageComponent } from './message.component';;
import { Routes } from '@angular/router';

export const messageRoutes: Routes = [
  { path: 'detail', component: MessageDetailComponent },
  { path: '', component: MessageComponent },
];
