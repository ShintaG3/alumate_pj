import { Component, OnInit } from '@angular/core';
import { faImage } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-post-comment-form',
  templateUrl: './post-comment-form.component.html',
  styleUrls: ['./post-comment-form.component.css']
})
export class PostCommentFormComponent implements OnInit {
  faImage = faImage;

  constructor() { }

  ngOnInit(): void {
  }

}
