import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyAbroadAddBtnComponent } from './study-abroad-add-btn.component';

describe('StudyAbroadAddBtnComponent', () => {
  let component: StudyAbroadAddBtnComponent;
  let fixture: ComponentFixture<StudyAbroadAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyAbroadAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyAbroadAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
