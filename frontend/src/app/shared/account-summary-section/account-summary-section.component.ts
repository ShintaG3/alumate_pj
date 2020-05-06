import { User } from './../../auths/auths.model';
import { ProfileImage, BasicInfo, Education } from './../../account/account.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-account-summary-section',
  templateUrl: './account-summary-section.component.html',
  styleUrls: ['./account-summary-section.component.css']
})
export class AccountSummarySectionComponent implements OnInit {
  @Input() basicInfo: BasicInfo;

  user: User;
  profileImage: ProfileImage;
  education: Education;

  logoUrl: string;
  followed = false;

  constructor() { }

  ngOnInit(): void {
    this.user = this.basicInfo.user;
    this.profileImage = {
      user: null,
      imageUrl: this.getProfileImageUrl()
    };
    this.logoUrl = this.getLogoUrl();
  }

  getProfileImageUrl(): string {
    return 'assets/img/placeholder.png';
  }

  getLogoUrl(): string {
    switch (this.basicInfo.status.value) {
      case 'FU': return 'assets/img/brand/logo_future.png';
      case 'CU': return 'assets/img/brand/logo_current.png';
      case 'AL': return 'assets/img/brand/logo_alumni.png';
      default: return null;
    }
  }

  follow(): void {
    console.log('follow!');
  }
}
