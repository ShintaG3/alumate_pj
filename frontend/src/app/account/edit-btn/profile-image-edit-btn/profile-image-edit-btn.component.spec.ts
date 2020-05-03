import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileImageEditBtnComponent } from './profile-image-edit-btn.component';

describe('ProfileImageEditBtnComponent', () => {
  let component: ProfileImageEditBtnComponent;
  let fixture: ComponentFixture<ProfileImageEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProfileImageEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfileImageEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
