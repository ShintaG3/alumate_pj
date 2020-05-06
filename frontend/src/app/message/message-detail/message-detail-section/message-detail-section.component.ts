import { ProfileImageService } from './../../../services/profile-image.service';
import { Message } from './../../message.model';
import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-message-detail-section',
  templateUrl: './message-detail-section.component.html',
  styleUrls: ['./message-detail-section.component.css']
})
export class MessageDetailSectionComponent implements OnInit {
  @Input() message: Message;
  profileImageUrl: string;

  constructor(
    private profileImageService: ProfileImageService
  ) { }

  ngOnInit(): void {
    this.profileImageUrl = this.profileImageService.getProfileImageUrl(null);
  }
}
