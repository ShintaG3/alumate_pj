import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-profile-image-edit-btn',
  templateUrl: './profile-image-edit-btn.component.html',
  styleUrls: ['./profile-image-edit-btn.component.css']
})
export class ProfileImageEditBtnComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
