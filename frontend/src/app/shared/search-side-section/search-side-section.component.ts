import { FormGroup, FormBuilder, FormArray, FormControl } from '@angular/forms';
import { School, Major, Country, CurrentStatus } from './../../account/account.model';
import { Component, OnInit } from '@angular/core';
import { Observable, Subject } from 'rxjs';
import { SliderValues } from '../input/slider-input/slider-input.component';

@Component({
  selector: 'app-search-side-section',
  templateUrl: './search-side-section.component.html',
  styleUrls: ['./search-side-section.component.css']
})
export class SearchSideSectionComponent implements OnInit {
  // for auto completes; fetch from backend
  statusChoices: CurrentStatus[];
  countryChoices: string[];
  schoolChoices: string[];
  majorChoices: string[];

  // filtering conditions
  selectedStatus: CurrentStatus[] = [];
  homeCountryTags: string[] = [];
  studyAbroadCountryTags: string[] = [];
  schoolTags: string[] = [];
  majorTags: string[] = [];
  startYearRange: SliderValues;
  endYearRange: SliderValues;

  constructor(private fb: FormBuilder) { }

  ngOnInit(): void {
    // mock data
    this.statusChoices = [
      {
        value: 'FU',
        displayName: 'Future Student'
      },
      {
        value: 'CU',
        displayName: 'Current Student'
      },
      {
        value: 'AL',
        displayName: 'Alumni'
      },
    ];
    this.majorChoices = ['Arts', 'Science', 'Business'];
    this.countryChoices = ['Japan', 'USA', 'Canada'];
    this.schoolChoices = ['UBC', 'UT', 'SFU'];
  }

  onStatusCheckboxChange(status: CurrentStatus, isChecked: boolean) {
    if (isChecked) {
      this.selectedStatus.push(status);
    } else {
      const index = this.selectedStatus.findIndex(x => x.value === status.value);
      this.selectedStatus.slice(index, 1);
    }
  }

  applyChange(): void {
    console.log('selectedStatus', this.selectedStatus);
    console.log('homeCountryTags', this.homeCountryTags);
    console.log('studyAbroadCountryTags', this.studyAbroadCountryTags);
    console.log('schoolTags', this.schoolTags);
    console.log('majorTags', this.majorTags);
    console.log('startYearRange', this.startYearRange);
    console.log('endYearRange', this.endYearRange);
  }

  onHomeCountryTagsChanged(newTags: string[]) {
    this.homeCountryTags = newTags;
  }

  onStudyAbroadCountryTagsChanged(newTags: string[]) {
    this.studyAbroadCountryTags = newTags;
  }

  onSchoolTagsChanged(newTags: string[]) {
    this.schoolTags = newTags;
  }

  onMajorTagsChanged(newTags: string[]) {
    this.majorTags = newTags;
  }

  onStartYearRangeChanged(newRange: SliderValues) {
    this.startYearRange = newRange;
  }

  onEndYearRangeChanged(newRange: SliderValues) {
    this.endYearRange = newRange;
  }
}
