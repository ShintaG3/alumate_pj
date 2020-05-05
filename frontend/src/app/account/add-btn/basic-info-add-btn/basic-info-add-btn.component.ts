import { BasicInfoModalComponent } from './../../modal/basic-info-modal/basic-info-modal.component';
import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';

@Component({
  selector: 'app-basic-info-add-btn',
  templateUrl: './basic-info-add-btn.component.html',
  styleUrls: ['./basic-info-add-btn.component.css']
})
export class BasicInfoAddBtnComponent implements OnInit {
  faPlus = faPlus;

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openModal(): void {
    const dialogConfig: MatDialogConfig = {
      disableClose: true
    };
    this.dialog.open(BasicInfoModalComponent, dialogConfig);
  }
}