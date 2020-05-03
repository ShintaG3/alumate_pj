import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PostCommentFormComponent } from './post-comment-form.component';

describe('PostCommentFormComponent', () => {
  let component: PostCommentFormComponent;
  let fixture: ComponentFixture<PostCommentFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PostCommentFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PostCommentFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
