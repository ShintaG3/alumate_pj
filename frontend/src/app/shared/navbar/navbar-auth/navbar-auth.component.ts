import { MenuModalComponent } from './../menu-modal/menu-modal.component';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-navbar-auth',
  templateUrl: './navbar-auth.component.html',
  styleUrls: ['./navbar-auth.component.css']
})
export class NavbarAuthComponent implements OnInit {
  constructor(private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  openMenuModal(): void {
    const dialogConfig: MatDialogConfig = {
      disableClose: false,
      maxWidth: '100%'
    };
    this.dialog.open(MenuModalComponent, dialogConfig);
  }
}
