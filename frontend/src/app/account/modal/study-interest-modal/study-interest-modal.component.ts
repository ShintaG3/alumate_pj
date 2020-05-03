import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-study-interest-modal',
  templateUrl: './study-interest-modal.component.html',
  styleUrls: ['./study-interest-modal.component.css']
})
export class StudyInterestModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
