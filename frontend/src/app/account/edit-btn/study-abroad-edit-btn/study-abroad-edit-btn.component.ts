import { StudyAbroad } from './../../account.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-study-abroad-edit-btn',
  templateUrl: './study-abroad-edit-btn.component.html',
  styleUrls: ['./study-abroad-edit-btn.component.css']
})
export class StudyAbroadEditBtnComponent implements OnInit {
  studyAbroad: StudyAbroad;

  constructor() { }

  ngOnInit(): void {
  }

}
