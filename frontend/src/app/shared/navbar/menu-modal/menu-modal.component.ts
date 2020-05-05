import { MatDialogRef } from '@angular/material/dialog';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-menu-modal',
  templateUrl: './menu-modal.component.html',
  styleUrls: ['./menu-modal.component.css']
})
export class MenuModalComponent implements OnInit {

  constructor(
    public dialogRef: MatDialogRef<MenuModalComponent>,
  ) {}

  ngOnInit(): void {
    this.dialogRef.updatePosition({ top: '0px' });
    this.dialogRef.updateSize('95%');
  }

  close(): void {
    this.dialogRef.close();
  }
}
