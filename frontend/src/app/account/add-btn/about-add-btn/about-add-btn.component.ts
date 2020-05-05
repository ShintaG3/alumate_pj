import { MatDialogConfig, MatDialog } from '@angular/material/dialog';
import { AboutModalComponent } from './../../modal/about-modal/about-modal.component';
import { Component, OnInit } from '@angular/core';
import { faPlus } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-about-add-btn',
  templateUrl: './about-add-btn.component.html',
  styleUrls: ['./about-add-btn.component.css']
})
export class AboutAddBtnComponent implements OnInit {
  faPlus = faPlus;

  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openModal(): void {
    const dialogConfig: MatDialogConfig = {
      disableClose: true
    };
    this.dialog.open(AboutModalComponent, dialogConfig);
  }
}
