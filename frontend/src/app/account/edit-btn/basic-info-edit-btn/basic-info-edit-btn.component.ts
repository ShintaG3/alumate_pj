import { BasicInfo } from './../../account.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-basic-info-edit-btn',
  templateUrl: './basic-info-edit-btn.component.html',
  styleUrls: ['./basic-info-edit-btn.component.css']
})
export class BasicInfoEditBtnComponent implements OnInit {

  isFollowing = false;
  basicInfo: BasicInfo;

  constructor() { }

  ngOnInit(): void {
  }

}
