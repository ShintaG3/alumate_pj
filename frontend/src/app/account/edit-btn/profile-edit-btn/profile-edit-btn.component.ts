import { Profile } from './../../account.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-profile-edit-btn',
  templateUrl: './profile-edit-btn.component.html',
  styleUrls: ['./profile-edit-btn.component.css']
})
export class ProfileEditBtnComponent implements OnInit {
  profile: Profile;
  
  constructor() { }

  ngOnInit(): void {
  }

}
