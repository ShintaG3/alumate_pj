import { Component, OnInit, Input } from '@angular/core';
import { About } from '../../account.model';

@Component({
  selector: 'app-about-edit-btn',
  templateUrl: './about-edit-btn.component.html',
  styleUrls: ['./about-edit-btn.component.css']
})
export class AboutEditBtnComponent implements OnInit {
  @Input() about: About;

  constructor() { }

  ngOnInit(): void {
  }

}
