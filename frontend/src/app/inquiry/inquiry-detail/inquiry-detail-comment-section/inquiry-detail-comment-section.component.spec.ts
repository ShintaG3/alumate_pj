import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryDetailCommentSectionComponent } from './inquiry-detail-comment-section.component';

describe('InquiryDetailCommentSectionComponent', () => {
  let component: InquiryDetailCommentSectionComponent;
  let fixture: ComponentFixture<InquiryDetailCommentSectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryDetailCommentSectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryDetailCommentSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
