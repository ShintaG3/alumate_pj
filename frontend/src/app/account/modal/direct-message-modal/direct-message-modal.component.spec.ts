import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DirectMessageModalComponent } from './direct-message-modal.component';

describe('DirectMessageModalComponent', () => {
  let component: DirectMessageModalComponent;
  let fixture: ComponentFixture<DirectMessageModalComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DirectMessageModalComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DirectMessageModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
