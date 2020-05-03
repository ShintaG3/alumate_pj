import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ScholarshipModalComponent } from './scholarship-modal.component';

describe('ScholarshipModalComponent', () => {
  let component: ScholarshipModalComponent;
  let fixture: ComponentFixture<ScholarshipModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ScholarshipModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ScholarshipModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
