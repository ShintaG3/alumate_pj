import { InquiryComponent } from './inquiry.component';
import { InquiryDetailComponent } from './inquiry-detail/inquiry-detail.component';
import { Routes } from '@angular/router';

export const inquiryRoutes: Routes = [
  { path: 'detail', component: InquiryDetailComponent },
  { path: '', component: InquiryComponent },
];
