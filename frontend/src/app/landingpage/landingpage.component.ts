import { Component, OnInit } from '@angular/core';
import { faUniversity } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-landingpage',
  templateUrl: './landingpage.component.html',
  styleUrls: ['./landingpage.component.css']
})
export class LandingpageComponent implements OnInit {
  faUniversity = faUniversity;

  constructor() { }

  ngOnInit(): void {
  }

}
