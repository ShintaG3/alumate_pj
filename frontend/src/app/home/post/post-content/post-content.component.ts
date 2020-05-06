import { Post, Comment } from './../post.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-post-content',
  templateUrl: './post-content.component.html',
  styleUrls: ['./post-content.component.css']
})
export class PostContentComponent implements OnInit {
  @Input() post: Post;
  comments: Comment[];

  commentShown = false;

  constructor() { }

  ngOnInit(): void {
  }

  displayComments(): void {
    this.commentShown = !this.commentShown;
  }

}
