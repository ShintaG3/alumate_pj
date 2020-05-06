import { CurrentStatus, Country } from './../account/account.model';
import { Injectable } from '@angular/core';
import { User } from '../auths/auths.model';

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor() { }

  getProfileImageUrl(user: User) {
    if (!user) {
      return 'assets/img/placeholder.png';
    }
  }

  getStatusOptions(): CurrentStatus[] {
    return [
      {
        value: 'FU',
        displayName: 'Future Student'
      },
      {
        value: 'CU',
        displayName: 'Current Student'
      },
      {
        value: 'AL',
        displayName: 'Alumni'
      },
    ];
  }

  getCountryOptions(): Country[] {
    return [
      {
        name: 'Japan'
      },
      {
        name: 'USA'
      },
      {
        name: 'Canada'
      }
    ];
  }
}
