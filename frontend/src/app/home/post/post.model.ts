import { User } from './../../auths/auths.model';

export interface Post {
  user: User;
  body: string;
  created_at: Date;
  image: File;
}

export interface Comment {
  user: User;
  post: Post;
  body: string;
  created_at: Date;
  image: File;
}
