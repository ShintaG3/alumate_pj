import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfileAddBtnComponent } from './profile-add-btn.component';

describe('ProfileAddBtnComponent', () => {
  let component: ProfileAddBtnComponent;
  let fixture: ComponentFixture<ProfileAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ProfileAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ProfileAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
