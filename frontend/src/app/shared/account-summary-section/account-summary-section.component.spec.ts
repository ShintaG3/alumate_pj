import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AccountSummarySectionComponent } from './account-summary-section.component';

describe('AccountSummarySectionComponent', () => {
  let component: AccountSummarySectionComponent;
  let fixture: ComponentFixture<AccountSummarySectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AccountSummarySectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AccountSummarySectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
