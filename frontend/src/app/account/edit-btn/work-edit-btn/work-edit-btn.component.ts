import { WorkExperience } from './../../account.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-work-edit-btn',
  templateUrl: './work-edit-btn.component.html',
  styleUrls: ['./work-edit-btn.component.css']
})
export class WorkEditBtnComponent implements OnInit {
  workExperience: WorkExperience;

  constructor() { }

  ngOnInit(): void {
  }

}
