import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-profile-modal',
  templateUrl: './profile-modal.component.html',
  styleUrls: ['./profile-modal.component.css']
})
export class ProfileModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
