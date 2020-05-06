import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryDetailListTagSectionComponent } from './inquiry-detail-list-tag-section.component';

describe('InquiryDetailListTagSectionComponent', () => {
  let component: InquiryDetailListTagSectionComponent;
  let fixture: ComponentFixture<InquiryDetailListTagSectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryDetailListTagSectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryDetailListTagSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
