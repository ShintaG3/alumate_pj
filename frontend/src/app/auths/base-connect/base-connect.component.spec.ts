import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { BaseConnectComponent } from './base-connect.component';

describe('BaseConnectComponent', () => {
  let component: BaseConnectComponent;
  let fixture: ComponentFixture<BaseConnectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ BaseConnectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(BaseConnectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
