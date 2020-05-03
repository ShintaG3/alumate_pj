import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkEducationEditBtnComponent } from './work-education-edit-btn.component';

describe('WorkEducationEditBtnComponent', () => {
  let component: WorkEducationEditBtnComponent;
  let fixture: ComponentFixture<WorkEducationEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkEducationEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkEducationEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
