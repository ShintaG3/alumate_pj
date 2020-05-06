import { User } from './../../auths/auths.model';
import { Message } from '../message.model';
import { Component, OnInit, Input } from '@angular/core';
import { ProfileImageService } from '../../services/profile-image.service';

@Component({
  selector: 'app-message-list-item',
  templateUrl: './message-list-item.component.html',
  styleUrls: ['./message-list-item.component.css']
})
export class MessageListItemComponent implements OnInit {
  @Input() message: Message;
  name: string;
  user: User;
  profileImageUrl: string;

  constructor(
    private profileImageService: ProfileImageService
  ) { }

  ngOnInit(): void {
    this.name = this.getName();
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(null);
  }

  getName() {
    // from basic info: sender is user ? or not ?
    return 'Hiroki Koketsu';
  }
}
