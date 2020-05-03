import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BasicInfoModalComponent } from './basic-info-modal.component';

describe('BasicInfoModalComponent', () => {
  let component: BasicInfoModalComponent;
  let fixture: ComponentFixture<BasicInfoModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BasicInfoModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BasicInfoModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
