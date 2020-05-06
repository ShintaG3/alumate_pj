import { FormControl } from '@angular/forms';
import { ProfileImageService } from './../../../../services/profile-image.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-post-comment-form',
  templateUrl: './post-comment-form.component.html',
  styleUrls: ['./post-comment-form.component.css']
})
export class PostCommentFormComponent implements OnInit {
  body = new FormControl();
  selectedFile: File;

  profileImageUrl: string;

  constructor(
    private profileImageService: ProfileImageService,
  ) { }

  ngOnInit(): void {
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(null);
  }

  onFileChanged(event: { target: HTMLInputElement; }) {
    this.selectedFile = event.target.files[0];
    console.log(this.selectedFile);
  }

}
