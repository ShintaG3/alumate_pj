import { InquiryLike, InquiryComment } from './../../inquiry.model';
import { ProfileImageService } from './../../../services/profile-image.service';
import { Component, OnInit, Input } from '@angular/core';
import { BasicInfo } from '../../../account/account.model';

@Component({
  selector: 'app-inquiry-detail-comment',
  templateUrl: './inquiry-detail-comment.component.html',
  styleUrls: ['./inquiry-detail-comment.component.css'],
})
export class InquiryDetailCommentComponent implements OnInit {
  @Input() comment: InquiryComment;
  likes: InquiryLike[] = [];

  basicInfo: BasicInfo;
  profileImageUrl: string;

  replyFormShown = false;

  constructor(
    private profileImageService: ProfileImageService
  ) {}

  ngOnInit(): void {
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(null);
    this.basicInfo = {
      user: {
        username: 'hkoketsu',
        email: 'hiroki@email.com',
        password: 'hiroki',
      },
      name: 'Hiroki Koketsu',
      status: {
        value: 'CU',
        displayName: 'Current Student',
      },
      homeCountry: {
        name: 'Japan',
      },
      studyAbroadCountry: {
        name: 'Canada',
      },
    };
  }

  displayReplyForm(): void {
    this.replyFormShown = !this.replyFormShown;
  }
}
