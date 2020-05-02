import { Component, OnInit } from '@angular/core';
import { faSlack } from '@fortawesome/free-brands-svg-icons'

@Component({
  selector: 'app-footer-white',
  templateUrl: './footer-white.component.html',
  styleUrls: ['./footer-white.component.css']
})
export class FooterWhiteComponent implements OnInit {
  faSlack = faSlack;
  constructor() { }

  ngOnInit(): void {
  }

}
