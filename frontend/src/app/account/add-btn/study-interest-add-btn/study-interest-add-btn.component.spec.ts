import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyInterestAddBtnComponent } from './study-interest-add-btn.component';

describe('StudyInterestAddBtnComponent', () => {
  let component: StudyInterestAddBtnComponent;
  let fixture: ComponentFixture<StudyInterestAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyInterestAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyInterestAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
