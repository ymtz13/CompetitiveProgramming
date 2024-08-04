#ls in/ | xargs -I FILE sh -c "cat in/FILE | ./submit04-sub > out04/FILE"
ls in/ | xargs -I FILE sh -c "cat in/FILE | python3 submit05-sub.py > out05/FILE"
