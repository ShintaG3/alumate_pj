import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BasicInfoEditBtnComponent } from './basic-info-edit-btn.component';

describe('BasicInfoEditBtnComponent', () => {
  let component: BasicInfoEditBtnComponent;
  let fixture: ComponentFixture<BasicInfoEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BasicInfoEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BasicInfoEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
