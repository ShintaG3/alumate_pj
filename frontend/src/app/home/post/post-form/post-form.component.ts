import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { faImage } from '@fortawesome/free-regular-svg-icons';

@Component({
  selector: 'app-post-form',
  templateUrl: './post-form.component.html',
  styleUrls: ['./post-form.component.css']
})
export class PostFormComponent implements OnInit {
  faImage = faImage;

  postForm = new FormGroup({
    body: new FormControl(),
    image: new FormControl()
  });

  constructor() { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    console.log(this.postForm.value);
  }

}
