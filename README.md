# ogre_db_project
OGRE DB Project

```sh
rsync -Pav -e "ssh -i $HOME/.ssh/framework.pem" ubuntu@ogre.dgbellomy.com:web ./
psql -h psql-1.c1so8qiqiw95.us-east-2.rds.amazonaws.com -U postgres -d ogre_test -a -f accounts.sql -W
```
