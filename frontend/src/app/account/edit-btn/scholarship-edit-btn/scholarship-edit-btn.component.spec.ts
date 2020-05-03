import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScholarshipEditBtnComponent } from './scholarship-edit-btn.component';

describe('ScholarshipEditBtnComponent', () => {
  let component: ScholarshipEditBtnComponent;
  let fixture: ComponentFixture<ScholarshipEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScholarshipEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScholarshipEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
