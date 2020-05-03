import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileImageModalComponent } from './profile-image-modal.component';

describe('ProfileImageModalComponent', () => {
  let component: ProfileImageModalComponent;
  let fixture: ComponentFixture<ProfileImageModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProfileImageModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfileImageModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
