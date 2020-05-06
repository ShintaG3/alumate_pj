import { Component, OnInit } from '@angular/core';
import { ProfileImageService } from '../../../../services/profile-image.service';

@Component({
  selector: 'app-post-comment',
  templateUrl: './post-comment.component.html',
  styleUrls: ['./post-comment.component.css']
})
export class PostCommentComponent implements OnInit {
  profileImageUrl: string;

  constructor(
    private profileImageService: ProfileImageService
  ) { }

  ngOnInit(): void {
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(null);
  }

}
