import { WorkModalComponent } from './../../modal/work-modal/work-modal.component';
import { Component, OnInit } from '@angular/core';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';

@Component({
  selector: 'app-work-add-btn',
  templateUrl: './work-add-btn.component.html',
  styleUrls: ['./work-add-btn.component.css']
})
export class WorkAddBtnComponent implements OnInit {
  faPlus = faPlus;

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openModal(): void {
    const dialogConfig: MatDialogConfig = {
      disableClose: true
    };
    this.dialog.open(WorkModalComponent, dialogConfig);
  }
}
