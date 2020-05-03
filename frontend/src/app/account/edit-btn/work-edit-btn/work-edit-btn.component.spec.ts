import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkEditBtnComponent } from './work-edit-btn.component';

describe('WorkEditBtnComponent', () => {
  let component: WorkEditBtnComponent;
  let fixture: ComponentFixture<WorkEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
