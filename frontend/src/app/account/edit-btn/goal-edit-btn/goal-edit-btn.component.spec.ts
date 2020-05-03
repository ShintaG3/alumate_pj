import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GoalEditBtnComponent } from './goal-edit-btn.component';

describe('GoalEditBtnComponent', () => {
  let component: GoalEditBtnComponent;
  let fixture: ComponentFixture<GoalEditBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GoalEditBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GoalEditBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
