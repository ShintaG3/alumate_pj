import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AboutAddBtnComponent } from './about-add-btn.component';

describe('AboutAddBtnComponent', () => {
  let component: AboutAddBtnComponent;
  let fixture: ComponentFixture<AboutAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AboutAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AboutAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
