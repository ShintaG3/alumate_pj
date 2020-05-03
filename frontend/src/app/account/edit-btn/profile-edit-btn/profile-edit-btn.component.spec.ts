import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileEditBtnComponent } from './profile-edit-btn.component';

describe('ProfileEditBtnComponent', () => {
  let component: ProfileEditBtnComponent;
  let fixture: ComponentFixture<ProfileEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProfileEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfileEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
