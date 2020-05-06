import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryDetailCommentFormComponent } from './inquiry-detail-comment-form.component';

describe('InquiryDetailCommentFormComponent', () => {
  let component: InquiryDetailCommentFormComponent;
  let fixture: ComponentFixture<InquiryDetailCommentFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryDetailCommentFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryDetailCommentFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
