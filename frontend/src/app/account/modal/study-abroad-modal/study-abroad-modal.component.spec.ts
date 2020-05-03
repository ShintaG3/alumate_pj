import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { StudyAbroadModalComponent } from './study-abroad-modal.component';

describe('StudyAbroadModalComponent', () => {
  let component: StudyAbroadModalComponent;
  let fixture: ComponentFixture<StudyAbroadModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ StudyAbroadModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(StudyAbroadModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
