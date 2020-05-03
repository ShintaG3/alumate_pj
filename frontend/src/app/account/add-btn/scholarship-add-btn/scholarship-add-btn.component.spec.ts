import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScholarshipAddBtnComponent } from './scholarship-add-btn.component';

describe('ScholarshipAddBtnComponent', () => {
  let component: ScholarshipAddBtnComponent;
  let fixture: ComponentFixture<ScholarshipAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScholarshipAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScholarshipAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
