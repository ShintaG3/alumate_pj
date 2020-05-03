import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyInterestModalComponent } from './study-interest-modal.component';

describe('StudyInterestModalComponent', () => {
  let component: StudyInterestModalComponent;
  let fixture: ComponentFixture<StudyInterestModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyInterestModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyInterestModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
