import { MessageDetailFormComponent } from './message/message-detail/message-detail-form/message-detail-form.component';
import { MessageDetailSectionComponent } from './message/message-detail/message-detail-section/message-detail-section.component';
import { WorkEditBtnComponent } from './account/edit-btn/work-edit-btn/work-edit-btn.component';
import { MaterialModule } from './shared/material/material.module';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgModule } from '@angular/core';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { Ng5SliderModule } from 'ng5-slider';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingpageComponent } from './landingpage/landingpage.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { FooterWhiteComponent } from './shared/footer-white/footer-white.component';
import { NavbarNonAuthComponent } from './shared/navbar/navbar-non-auth/navbar-non-auth.component';
import { SignupComponent } from './auths/signup/signup.component';
import { LoginComponent } from './auths/login/login.component';
import { HomeComponent } from './home/home.component';
import { PostComponent } from './home/post/post.component';
import { AskComponent } from './home/ask/ask.component';
import { NavbarAuthComponent } from './shared/navbar/navbar-auth/navbar-auth.component';
import { LikeBtnComponent } from './shared/button/like-btn/like-btn.component';
import { ReplyBtnComponent } from './shared/button/reply-btn/reply-btn.component';
import { ShareBtnComponent } from './shared/button/share-btn/share-btn.component';
import { PostFormComponent } from './home/post/post-form/post-form.component';
import { PostContentComponent } from './home/post/post-content/post-content.component';
import { PostCommentComponent } from './home/post/post-content/post-comment/post-comment.component';
import { PostCommentFormComponent } from './home/post/post-content/post-comment-form/post-comment-form.component';
import { AccountComponent } from './account/account.component';
import { BasicInfoModalComponent } from './account/modal/basic-info-modal/basic-info-modal.component';
import { AboutModalComponent } from './account/modal/about-modal/about-modal.component';
import { WorkModalComponent } from './account/modal/work-modal/work-modal.component';
import { EducationModalComponent } from './account/modal/education-modal/education-modal.component';
import { GoalModalComponent } from './account/modal/goal-modal/goal-modal.component';
import { StudyInterestModalComponent } from './account/modal/study-interest-modal/study-interest-modal.component';
import { ScholarshipModalComponent } from './account/modal/scholarship-modal/scholarship-modal.component';
import { SocialLinkModalComponent } from './account/modal/social-link-modal/social-link-modal.component';
import { ProfileModalComponent } from './account/modal/profile-modal/profile-modal.component';
import { ProfileImageModalComponent } from './account/modal/profile-image-modal/profile-image-modal.component';
import { BasicInfoAddBtnComponent } from './account/add-btn/basic-info-add-btn/basic-info-add-btn.component';
import { AboutAddBtnComponent } from './account/add-btn/about-add-btn/about-add-btn.component';
import { WorkAddBtnComponent } from './account/add-btn/work-add-btn/work-add-btn.component';
import { EducationAddBtnComponent } from './account/add-btn/education-add-btn/education-add-btn.component';
import { StudyInterestAddBtnComponent } from './account/add-btn/study-interest-add-btn/study-interest-add-btn.component';
import { GoalAddBtnComponent } from './account/add-btn/goal-add-btn/goal-add-btn.component';
import { ScholarshipAddBtnComponent } from './account/add-btn/scholarship-add-btn/scholarship-add-btn.component';
import { ProfileAddBtnComponent } from './account/add-btn/profile-add-btn/profile-add-btn.component';
import { SocialLinkAddBtnComponent } from './account/add-btn/social-link-add-btn/social-link-add-btn.component';
import { StudyAbroadAddBtnComponent } from './account/add-btn/study-abroad-add-btn/study-abroad-add-btn.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { BasicInfoEditBtnComponent } from './account/edit-btn/basic-info-edit-btn/basic-info-edit-btn.component';
import { GoalEditBtnComponent } from './account/edit-btn/goal-edit-btn/goal-edit-btn.component';
import { WorkEducationEditBtnComponent } from './account/edit-btn/work-education-edit-btn/work-education-edit-btn.component';
import { StudyInterestEditBtnComponent } from './account/edit-btn/study-interest-edit-btn/study-interest-edit-btn.component';
import { StudyAbroadEditBtnComponent } from './account/edit-btn/study-abroad-edit-btn/study-abroad-edit-btn.component';
import { SocialLinkEditBtnComponent } from './account/edit-btn/social-link-edit-btn/social-link-edit-btn.component';
import { ScholarshipEditBtnComponent } from './account/edit-btn/scholarship-edit-btn/scholarship-edit-btn.component';
import { ProfileImageEditBtnComponent } from './account/edit-btn/profile-image-edit-btn/profile-image-edit-btn.component';
import { ProfileEditBtnComponent } from './account/edit-btn/profile-edit-btn/profile-edit-btn.component';
import { EducationEditBtnComponent } from './account/edit-btn/education-edit-btn/education-edit-btn.component';
import { AboutEditBtnComponent } from './account/edit-btn/about-edit-btn/about-edit-btn.component';
import { StudyAbroadModalComponent } from './account/modal/study-abroad-modal/study-abroad-modal.component';
import { DirectMessageModalComponent } from './account/modal/direct-message-modal/direct-message-modal.component';
import { InquiryComponent } from './inquiry/inquiry.component';
import { MessageComponent } from './message/message.component';
import { PeopleComponent } from './people/people.component';
import { SearchSectionComponent } from './shared/search-section/search-section.component';
import { MenuModalComponent } from './shared/navbar/menu-modal/menu-modal.component';
import { ChipsInputComponent } from './shared/input/chips-input/chips-input.component';
import { SliderInputComponent } from './shared/input/slider-input/slider-input.component';
import { PeopleResultSectionComponent } from './people/people-result-section/people-result-section.component';
import { AccountSummarySectionComponent } from './shared/account-summary-section/account-summary-section.component';
import { SearchModalComponent } from './shared/search-modal/search-modal.component';
import { InquiryResultSectionComponent } from './inquiry/inquiry-result-section/inquiry-result-section.component';
import { InquiryCardComponent } from './inquiry/inquiry-card/inquiry-card.component';
import { MessageModalComponent } from './message/message-modal/message-modal.component';
import { MessageListItemComponent } from './message/message-list-item/message-list-item.component';
import { MessageDetailComponent } from './message/message-detail/message-detail.component';
import { InquiryDetailComponent } from './inquiry/inquiry-detail/inquiry-detail.component';
import { InquiryDetailListTagSectionComponent } from './inquiry/inquiry-detail/inquiry-detail-list-tag-section/inquiry-detail-list-tag-section.component';
import { InquiryDetailListTagComponent } from './inquiry/inquiry-detail/inquiry-detail-list-tag/inquiry-detail-list-tag.component';
import { InquiryDetailCommentSectionComponent } from './inquiry/inquiry-detail/inquiry-detail-comment-section/inquiry-detail-comment-section.component';
import { InquiryDetailCommentFormComponent } from './inquiry/inquiry-detail/inquiry-detail-comment-form/inquiry-detail-comment-form.component';
import { InquiryDetailCommentComponent } from './inquiry/inquiry-detail/inquiry-detail-comment/inquiry-detail-comment.component';
import { AskContentComponent } from './home/ask/ask-content/ask-content.component';
import { AskFormComponent } from './home/ask/ask-form/ask-form.component';
import { BaseConnectComponent } from './auths/base-connect/base-connect.component';
import { BaseInquiryComponent } from './auths/base-inquiry/base-inquiry.component';
import { BaseInquiryFormComponent } from './auths/base-inquiry/base-inquiry-form/base-inquiry-form.component';
import { ContactComponent } from './contact/contact.component';
import { ContactFormComponent } from './contact/contact-form/contact-form.component';


@NgModule({
  declarations: [
    AppComponent,
    LandingpageComponent,
    FooterWhiteComponent,
    NavbarNonAuthComponent,
    SignupComponent,
    LoginComponent,
    HomeComponent,
    PostComponent,
    AskComponent,
    NavbarAuthComponent,
    LikeBtnComponent,
    ReplyBtnComponent,
    ShareBtnComponent,
    PostFormComponent,
    PostContentComponent,
    PostCommentComponent,
    PostCommentFormComponent,
    AccountComponent,
    BasicInfoModalComponent,
    AboutModalComponent,
    WorkModalComponent,
    EducationModalComponent,
    GoalModalComponent,
    StudyInterestModalComponent,
    StudyAbroadModalComponent,
    ScholarshipModalComponent,
    SocialLinkModalComponent,
    ProfileModalComponent,
    ProfileImageModalComponent,
    BasicInfoAddBtnComponent,
    AboutAddBtnComponent,
    WorkAddBtnComponent,
    EducationAddBtnComponent,
    StudyInterestAddBtnComponent,
    GoalAddBtnComponent,
    ScholarshipAddBtnComponent,
    ProfileAddBtnComponent,
    SocialLinkAddBtnComponent,
    StudyAbroadAddBtnComponent,
    AboutEditBtnComponent,
    BasicInfoEditBtnComponent,
    EducationEditBtnComponent,
    GoalEditBtnComponent,
    ProfileEditBtnComponent,
    ProfileImageEditBtnComponent,
    ScholarshipEditBtnComponent,
    SocialLinkEditBtnComponent,
    StudyAbroadEditBtnComponent,
    StudyInterestEditBtnComponent,
    WorkEducationEditBtnComponent,
    WorkEditBtnComponent,
    DirectMessageModalComponent,
    InquiryComponent,
    MessageComponent,
    PeopleComponent,
    SearchSectionComponent,
    MenuModalComponent,
    ChipsInputComponent,
    SliderInputComponent,
    PeopleResultSectionComponent,
    AccountSummarySectionComponent,
    SearchModalComponent,
    InquiryResultSectionComponent,
    InquiryCardComponent,
    MessageModalComponent,
    MessageListItemComponent,
    MessageDetailComponent,
    MessageDetailSectionComponent,
    MessageDetailFormComponent,
    InquiryDetailComponent,
    InquiryDetailListTagSectionComponent,
    InquiryDetailListTagComponent,
    InquiryDetailCommentSectionComponent,
    InquiryDetailCommentFormComponent,
    InquiryDetailCommentComponent,
    AskContentComponent,
    AskFormComponent,
    BaseConnectComponent,
    BaseInquiryComponent,
    BaseInquiryFormComponent,
    ContactComponent,
    ContactFormComponent,
  ],
  imports: [
    NgbModule,
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    FontAwesomeModule,
    FormsModule,
    NgSelectModule,
    Ng5SliderModule,
    MaterialModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
