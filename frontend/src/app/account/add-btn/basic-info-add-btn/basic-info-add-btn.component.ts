import { Component, OnInit } from '@angular/core';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-basic-info-add-btn',
  templateUrl: './basic-info-add-btn.component.html',
  styleUrls: ['./basic-info-add-btn.component.css']
})
export class BasicInfoAddBtnComponent implements OnInit {
  faPlus = faPlus;

  constructor() { }

  ngOnInit(): void {
  }

}
