import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { GoalAddBtnComponent } from './goal-add-btn.component';

describe('GoalAddBtnComponent', () => {
  let component: GoalAddBtnComponent;
  let fixture: ComponentFixture<GoalAddBtnComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ GoalAddBtnComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(GoalAddBtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
