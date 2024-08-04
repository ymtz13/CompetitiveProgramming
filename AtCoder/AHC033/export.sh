#ls in/ | xargs -I FILE sh -c "cat in/FILE | ./submit04-sub > out04/FILE"
ls in/ | xargs -I FILE sh -c "cat in/FILE | ./ssub04 > out04/FILE"
