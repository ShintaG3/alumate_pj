import { BasicInfo, About, Goal, StudyInterest } from './account.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  hasEditPermission = true;
  isFollowing = false;

  basicInfo: BasicInfo = {
    user: null,
    name: 'Hiroki',
    status: 'Current',
    homeCountry: {
      name: 'Japan',
    },
    studyAbroadCountry: {
      name: 'Canada'
    }
  };
  about: About;
  expHistory: any[];
  goals: Goal[];
  studyInterests: StudyInterest[];
  scholarshipHistory: any[];


  constructor() { }

  ngOnInit(): void {
  }

}
