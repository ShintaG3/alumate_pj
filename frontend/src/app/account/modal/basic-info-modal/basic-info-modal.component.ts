import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-basic-info-modal',
  templateUrl: './basic-info-modal.component.html',
  styleUrls: ['./basic-info-modal.component.css']
})
export class BasicInfoModalComponent implements OnInit {
  basicInfoForm: FormGroup;

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.basicInfoForm = this.fb.group({
      name: [''],
      status: [''],
      homeCountry: [''],
      studyAbroadCountry: ['']
    });
  }
}
