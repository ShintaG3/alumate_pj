import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EducationEditBtnComponent } from './education-edit-btn.component';

describe('EducationEditBtnComponent', () => {
  let component: EducationEditBtnComponent;
  let fixture: ComponentFixture<EducationEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EducationEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EducationEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
