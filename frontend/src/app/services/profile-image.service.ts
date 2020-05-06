import { User } from './../auths/auths.model';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProfileImageService {

  constructor() { }

  getProfileImageUrl(user: User) {
    if (!user) {
      return 'assets/img/placeholder.png';
    }
  }
}
