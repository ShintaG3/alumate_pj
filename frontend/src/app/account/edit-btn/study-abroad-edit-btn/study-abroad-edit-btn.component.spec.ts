import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyAbroadEditBtnComponent } from './study-abroad-edit-btn.component';

describe('StudyAbroadEditBtnComponent', () => {
  let component: StudyAbroadEditBtnComponent;
  let fixture: ComponentFixture<StudyAbroadEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyAbroadEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyAbroadEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
