import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { InquiryDetailListTagComponent } from './inquiry-detail-list-tag.component';

describe('InquiryDetailListTagComponent', () => {
  let component: InquiryDetailListTagComponent;
  let fixture: ComponentFixture<InquiryDetailListTagComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ InquiryDetailListTagComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(InquiryDetailListTagComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
