import { User } from './../../../auths/auths.model';
import { ProfileImageService } from './../../../services/profile-image.service';
import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-inquiry-detail-comment-form',
  templateUrl: './inquiry-detail-comment-form.component.html',
  styleUrls: ['./inquiry-detail-comment-form.component.css']
})
export class InquiryDetailCommentFormComponent implements OnInit {
  profileImageUrl: string;
  user: User;

  body = new FormControl('');
  selectedFile: File;

  constructor(private profileImageService: ProfileImageService) { }

  ngOnInit(): void {
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(this.user);
  }

  onFileChanged(event: { target: HTMLInputElement; }) {
    this.selectedFile = event.target.files[0];
    console.log(this.selectedFile);
  }

  send() {
    console.log('send message', this.body.value, this.selectedFile.name);
  }
}
