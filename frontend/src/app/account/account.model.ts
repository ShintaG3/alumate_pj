import { User } from './../auths/auths.model';
import { Url } from 'url';

export interface BasicInfo {
  user: User;
  name: string;
  status: string;
  homeCountry: Country;
  studyAbroadCountry: Country;
}

export interface Profile {
  user: User;
  gender: string;
  birthday: Date;
}

export interface ProfileImage {
  user: User;
  image: File;
}

export interface Goal {
  user: User;
  body: string;
}

export interface StudyInterest {
  user: User;
  body: string;
}

export interface About {
  user: User;
  body: string;
}

export interface Education {
  user: User;
  school: School;
  degree: string;
  major: Major;
  isStudyAbroad: boolean;
  startYear: string;
  endYear: string;
}

export interface School {
  name: string;
}

export interface Country {
  name: string;
}

export interface Major {
  name: string;
}

export interface StudyAbroad {
  user: User;
  education: Education;
}

export interface WorkExperience {
  user: User;
  company: string;
  position: string;
  startYear: string;
  endYear: string;
}

export interface Scholarship {
  user: User;
  organization: string;
  title: string;
}

export interface SocialLink {
  user: User;
  title: string;
  url: Url;
}

export interface City {
  name: string;
  country: Country;
}

export interface Follow {
  follower: User;
  following: User;
}
