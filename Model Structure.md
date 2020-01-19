## User_profiles
 user FK  
 school_start_year  
 school_end_year country Choose  
 course Char  
 previous_job   
 pre_jog_start_year  
 pre_job_end_year 
 post_job  
 liveing_country  living_city  
 created_at  
 slug  
 status choose
 followings  
 followers  
 description

## Schools
 name  
 user_profiles one2M  
 country Choose  
 slug  


## Posts
 user_profiles FK  
 discription  
 img  
 created_at  
 ask Boolean  
 slug



## Comments
 user fk  
 post fk  
 discription  
 created_at  


## Likes_to_post
 post fk  
 user fk 

## Likes_to_comment
 comment fk  
 user fk


## Tags
 post FK  
 country_tag manytomany  
 school_tag manytomany  
 status_tag manytomany  
 job_tag Char  
 other_tag Char  

## Rooms
slug  
receiver FK  
sender FK

## Messags
room FK  
sender FK  
text  
timestamp



