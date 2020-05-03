import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkAddBtnComponent } from './work-add-btn.component';

describe('WorkAddBtnComponent', () => {
  let component: WorkAddBtnComponent;
  let fixture: ComponentFixture<WorkAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
