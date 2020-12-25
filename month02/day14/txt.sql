alter table friend_circle add constraint user_fk foreign key (user_id) references userinfo(id));
