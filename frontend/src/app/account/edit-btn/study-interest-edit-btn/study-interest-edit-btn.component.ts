import { StudyInterest } from './../../account.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-study-interest-edit-btn',
  templateUrl: './study-interest-edit-btn.component.html',
  styleUrls: ['./study-interest-edit-btn.component.css']
})
export class StudyInterestEditBtnComponent implements OnInit {
  @Input() studyInterests: StudyInterest[];

  constructor() { }

  ngOnInit(): void {
  }

}
