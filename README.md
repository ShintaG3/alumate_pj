Alumate
===
Overview
---
Alumate is a social platform which helps people who is preparing for study abroad, current students, and alumni.

Milestones
---
- Complete the Resistration/Login/Logout, Profile, Search, Follow
- Complete the Post, Like, Comment, Notification 
- Complete the Inquiry Post, Inquiry Page
- Complete the Private message
- Complete the Premium, Subscription method

Requirements
---

Alumate shall have followinig fanctionalities.
- **Sign in**: User can sign-in from social apps. After signup, user fill their profile information, then connect existing users.  
**considering plugin**: oath2, allauth
- **User account**: User can sign-up and create own account. Profile includes: country, school, course, start-year, end-year, student status(preparing, current, alumni), previous education(school), previous job, post job, livinig location.  
**model**: AUTH_USER
- **User search**: User can search other users by: country, school, start/end year, job, living location, and follow them.
- **Feed**: User can post and see following users' posts in their feed page. In a post, user can like and comment.
- **Feed search**: There is a search box for feed
- **Notification**: When user receive like and comment on their posts, notification badge apears on the navigation bar.
- **Inquiry**: User can make a inquiry to target  users by tagging profile information. e.g. Harvard University, 2020. These inquiries appear on the feed page of the target users, regardless of following. Also, there is a inquiry page where all inquiry can be seen and searched.
- **Private Message**: User can send private message to other users.

Additional features (Pending until above features are done)
---
- **Mentor**: User can be a mentor who can intensively support other users for certain duration.
- **Restriction**: Free subscription user can send messages to only same status or less users. They cannot request mentor suport.
- **Premium**: Premium user can send message all users and can request mentor suport.

Deployment
---
Heroku

Mediafile storage
---
AWS