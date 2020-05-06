import { AccountService } from './../../services/account.service';
import { Message } from './../message.model';
import { BasicInfo } from './../../account/account.model';
import { User } from './../../auths/auths.model';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-message-detail',
  templateUrl: './message-detail.component.html',
  styleUrls: ['./message-detail.component.css']
})
export class MessageDetailComponent implements OnInit {
  profileImageUrl: string;
  sender: User;
  senderBasicInfo: BasicInfo;
  messages: Message[];

  constructor(
    private accountService: AccountService
  ) { }

  ngOnInit(): void {
    this.profileImageUrl = this.accountService.getProfileImageUrl(null);
    this.messages = [
      {
        sender: {
          username: 'hkoketsu',
          email: 'hiroki@email.com',
          password: 'hiroki'
        },
        receiver: {
          username: 'hoge',
          email: 'hiroki@email.com',
          password: 'hiroki'
        },
        body: 'Hi',
        created_at: new Date()
      },
      {
        sender: {
          username: 'hoge',
          email: 'hiroki@email.com',
          password: 'hiroki'
        },
        receiver: {
          username: 'hkoketsu',
          email: 'hiroki@email.com',
          password: 'hiroki'
        },
        body: 'Hello',
        created_at: new Date()
      },
    ]
  }

}
