import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryResultSectionComponent } from './inquiry-result-section.component';

describe('InquiryResultSectionComponent', () => {
  let component: InquiryResultSectionComponent;
  let fixture: ComponentFixture<InquiryResultSectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryResultSectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryResultSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
