import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-social-link-edit-btn',
  templateUrl: './social-link-edit-btn.component.html',
  styleUrls: ['./social-link-edit-btn.component.css']
})
export class SocialLinkEditBtnComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
