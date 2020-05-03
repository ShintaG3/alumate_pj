import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutEditBtnComponent } from './about-edit-btn.component';

describe('AboutEditBtnComponent', () => {
  let component: AboutEditBtnComponent;
  let fixture: ComponentFixture<AboutEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AboutEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
