import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { concat, Observable, of, Subject } from 'rxjs';
import { catchError, debounceTime, distinctUntilChanged, switchMap, tap } from 'rxjs/operators';
import { Options } from 'ng5-slider';

interface Country {
  id: number;
  name: string;
}
interface School {
  id: number;
  name: string;
}
interface Major {
  id: number;
  name: string;
}
@Component({
  selector: 'app-ask',
  templateUrl: './ask.component.html',
  styleUrls: ['./ask.component.css'],
})
export class AskComponent implements OnInit {
  selectedHomeCountries = [];
  selectedStudyAbroadCountries = [];
  selectedSchools = [];
  selectedMajors = [];

  countries = [
    {
      id: 1,
      name: 'Japan',
    },
    {
      id: 2,
      name: 'USA',
    },
    {
      id: 3,
      name: 'Canada',
    },
  ];

  schools$: Observable<School[]>;
  schoolInput$ = new Subject<string>();
  schoolLoading = false;

  majors = [
    {
      id: 1,
      name: 'Arts',
    },
    {
      id: 2,
      name: 'Science',
    },
    {
      id: 3,
      name: 'Business',
    },
  ];



  constructor() {}

  ngOnInit(): void {
    this.loadSchools();
  }

  trackByFn(item: School) {
    return item.id;
  }

  private loadSchools() {
    // this.schools$ = concat(
    //     of([]), // default items
    //     this.schoolsInput$.pipe(
    //         distinctUntilChanged(),
    //         tap(() => this.schoolLoading = true),
    //         switchMap(term => this.dataService.getPeople(term).pipe(
    //             catchError(() => of([])), // empty list on error
    //             tap(() => this.schoolLoading = false)
    //         ))
    //     )
    // );
  }
}
