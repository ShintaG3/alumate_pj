import { BasicInfo, Country } from './../../account.model';
import { Component, OnInit, Inject } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'app-basic-info-modal',
  templateUrl: './basic-info-modal.component.html',
  styleUrls: ['./basic-info-modal.component.css']
})
export class BasicInfoModalComponent implements OnInit {
  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    public dialogRef: MatDialogRef<BasicInfoModalComponent>,
    ) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      name: [''],
      status: [''],
      homeCountry: [''],
      studyAbroadCountry: ['']
    });
  }

  save(): void {
    this.dialogRef.close(this.form.value);
  }

  cancel(): void {
    this.dialogRef.close();
  }
}
