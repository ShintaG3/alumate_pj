import { AccountService } from './../../../services/account.service';
import { CurrentStatus, Country } from './../../../account/account.model';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-base-inquiry-form',
  templateUrl: './base-inquiry-form.component.html',
  styleUrls: ['./base-inquiry-form.component.css']
})
export class BaseInquiryFormComponent implements OnInit {
  form: FormGroup;

  statusChoices: CurrentStatus[];
  countryChoices: Country[];

  constructor(
    private fb: FormBuilder,
    private router: Router,
    private accountService: AccountService,
  ) { }

  ngOnInit(): void {
    this.statusChoices = this.accountService.getStatusOptions();
    this.countryChoices = this.accountService.getCountryOptions();
    this.form = this.fb.group({
      name: [''],
      status: [],
      homeCountry: [],
      studyAbroadCountry: []
    });
  }

  next(): void {
    console.log(this.form.value);
    this.router.navigate(['/auths/base-connect']);
  }
}
