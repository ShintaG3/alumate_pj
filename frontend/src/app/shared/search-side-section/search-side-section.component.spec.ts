import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SearchSideSectionComponent } from './search-side-section.component';

describe('SearchSideSectionComponent', () => {
  let component: SearchSideSectionComponent;
  let fixture: ComponentFixture<SearchSideSectionComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SearchSideSectionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SearchSideSectionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
