import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyInterestEditBtnComponent } from './study-interest-edit-btn.component';

describe('StudyInterestEditBtnComponent', () => {
  let component: StudyInterestEditBtnComponent;
  let fixture: ComponentFixture<StudyInterestEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyInterestEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyInterestEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
