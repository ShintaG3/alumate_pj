import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-social-link-modal',
  templateUrl: './social-link-modal.component.html',
  styleUrls: ['./social-link-modal.component.css']
})
export class SocialLinkModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  constructor() { }

  ngOnInit(): void {
  }

}
