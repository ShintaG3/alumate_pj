import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryDetailCommentComponent } from './inquiry-detail-comment.component';

describe('InquiryDetailCommentComponent', () => {
  let component: InquiryDetailCommentComponent;
  let fixture: ComponentFixture<InquiryDetailCommentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryDetailCommentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryDetailCommentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
