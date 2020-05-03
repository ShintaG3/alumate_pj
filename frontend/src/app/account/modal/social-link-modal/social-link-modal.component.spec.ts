import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SocialLinkModalComponent } from './social-link-modal.component';

describe('SocialLinkModalComponent', () => {
  let component: SocialLinkModalComponent;
  let fixture: ComponentFixture<SocialLinkModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SocialLinkModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SocialLinkModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
