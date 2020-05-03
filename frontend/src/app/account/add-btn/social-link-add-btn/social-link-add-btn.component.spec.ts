import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SocialLinkAddBtnComponent } from './social-link-add-btn.component';

describe('SocialLinkAddBtnComponent', () => {
  let component: SocialLinkAddBtnComponent;
  let fixture: ComponentFixture<SocialLinkAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SocialLinkAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SocialLinkAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
