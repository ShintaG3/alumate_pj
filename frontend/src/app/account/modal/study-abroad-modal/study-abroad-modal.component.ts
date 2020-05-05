import { StudyAbroad } from './../../account.model';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Component, OnInit, Input, Inject } from '@angular/core';
import { MatDialogRef, MAT_DIALOG_DATA } from '@angular/material/dialog';

@Component({
  selector: 'app-study-abroad-modal',
  templateUrl: './study-abroad-modal.component.html',
  styleUrls: ['./study-abroad-modal.component.css']
})
export class StudyAbroadModalComponent implements OnInit {
  @Input() hasEditPermission: boolean;

  form: FormGroup;

  constructor(
    private fb: FormBuilder,
    public dialogRef: MatDialogRef<StudyAbroadModalComponent>,
    @Inject(MAT_DIALOG_DATA) public data: StudyAbroad
    ) {}

  ngOnInit(): void {
    this.form = this.fb.group({
      name: [''],
      status: [],
      homeCountry: [],
      studyAbroadCountry: []
    });
  }

  save(): void {
    this.dialogRef.close(this.form.value);
  }

  cancel(): void {
    this.dialogRef.close();
  }

}
