import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SocialLinkEditBtnComponent } from './social-link-edit-btn.component';

describe('SocialLinkEditBtnComponent', () => {
  let component: SocialLinkEditBtnComponent;
  let fixture: ComponentFixture<SocialLinkEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SocialLinkEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SocialLinkEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
