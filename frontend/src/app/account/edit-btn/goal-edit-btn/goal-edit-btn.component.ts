import { Goal } from './../../account.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-goal-edit-btn',
  templateUrl: './goal-edit-btn.component.html',
  styleUrls: ['./goal-edit-btn.component.css']
})
export class GoalEditBtnComponent implements OnInit {
  @Input() goals: Goal[];

  constructor() { }

  ngOnInit(): void {
  }

}
