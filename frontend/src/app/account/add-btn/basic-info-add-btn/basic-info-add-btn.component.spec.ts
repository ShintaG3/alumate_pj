import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BasicInfoAddBtnComponent } from './basic-info-add-btn.component';

describe('BasicInfoAddBtnComponent', () => {
  let component: BasicInfoAddBtnComponent;
  let fixture: ComponentFixture<BasicInfoAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BasicInfoAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BasicInfoAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
