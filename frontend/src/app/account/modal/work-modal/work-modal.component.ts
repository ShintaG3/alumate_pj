import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-work-modal',
  templateUrl: './work-modal.component.html',
  styleUrls: ['./work-modal.component.css']
})
export class WorkModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;
  
  constructor() { }

  ngOnInit(): void {
  }

}
