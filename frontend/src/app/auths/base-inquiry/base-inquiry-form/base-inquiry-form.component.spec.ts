import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BaseInquiryFormComponent } from './base-inquiry-form.component';

describe('BaseInquiryFormComponent', () => {
  let component: BaseInquiryFormComponent;
  let fixture: ComponentFixture<BaseInquiryFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BaseInquiryFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BaseInquiryFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
