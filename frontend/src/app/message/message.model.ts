import { User } from './../auths/auths.model';

export interface Message {
  sender: User;
  receiver: User;
  body: string;
  created_at: Date;
}
