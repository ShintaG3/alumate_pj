import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { EducationAddBtnComponent } from './education-add-btn.component';

describe('EducationAddBtnComponent', () => {
  let component: EducationAddBtnComponent;
  let fixture: ComponentFixture<EducationAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ EducationAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(EducationAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
