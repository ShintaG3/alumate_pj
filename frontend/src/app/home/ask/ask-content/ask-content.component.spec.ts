import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AskContentComponent } from './ask-content.component';

describe('AskContentComponent', () => {
  let component: AskContentComponent;
  let fixture: ComponentFixture<AskContentComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AskContentComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AskContentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
