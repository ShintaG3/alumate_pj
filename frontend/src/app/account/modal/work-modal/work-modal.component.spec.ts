import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkModalComponent } from './work-modal.component';

describe('WorkModalComponent', () => {
  let component: WorkModalComponent;
  let fixture: ComponentFixture<WorkModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WorkModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WorkModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
