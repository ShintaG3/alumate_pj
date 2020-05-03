import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-study-abroad-modal',
  templateUrl: './study-abroad-modal.component.html',
  styleUrls: ['./study-abroad-modal.component.css']
})
export class StudyAbroadModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
