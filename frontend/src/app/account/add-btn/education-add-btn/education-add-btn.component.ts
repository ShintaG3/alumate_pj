import { EducationModalComponent } from './../../modal/education-modal/education-modal.component';
import { Component, OnInit } from '@angular/core';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';

@Component({
  selector: 'app-education-add-btn',
  templateUrl: './education-add-btn.component.html',
  styleUrls: ['./education-add-btn.component.css']
})
export class EducationAddBtnComponent implements OnInit {
  faPlus = faPlus;

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openModal(): void {
    const dialogConfig: MatDialogConfig = {
      disableClose: true
    };
    this.dialog.open(EducationModalComponent, dialogConfig);
  }
}
