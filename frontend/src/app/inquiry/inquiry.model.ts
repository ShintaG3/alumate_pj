import { User } from './../auths/auths.model';

export interface Inquiry {
  user: User;
  title: string;
  body: string;
  created_at: Date;
}

export interface InquiryLike {
  user: User;
  inquiry: Inquiry;
}

export interface InquiryComment {
  user: User;
  inquiry: Inquiry;
  body: string;
  created_at: Date;
}

export interface Tag {
  body: string;
}
