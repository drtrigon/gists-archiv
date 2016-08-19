# gists-archiv
Archives of outdated gist repos

# Instructions
> $ git clone https://github.com/drtrigon/gists-archiv.git
> $ cd gists-archiv/
> $ wget https://api.github.com/users/drtrigon/gists
> $ cd ..

> $ git clone https://gist.github.com/b7d367514745715fff332b652349f222.git
> $ cd b7d367514745715fff332b652349f222/
> $ mkdir b7d367514745715fff332b652349f222
> $ mv !(b7d367514745715fff332b652349f222) b7d367514745715fff332b652349f222
> $ cd b7d367514745715fff332b652349f222/
> $ wget https://api.github.com/gists/b7d367514745715fff332b652349f222/comments
> $ cd ..
> $ git add --all
> $ git config user.email "dr.trigon@surfeu.ch"
> $ git config user.name "drtrigon"
> $ git commit -m "Preparing obsolete gist project for archiv"
> 
> $ cd ../gists-archiv/
> $ git remote add b7d367514745715fff332b652349f222 /home/osboxes/b7d367514745715fff332b652349f222/ 
> $ git fetch b7d367514745715fff332b652349f222
> $ git config user.email "dr.trigon@surfeu.ch"
> $ git config user.name "drtrigon"
> $ git merge b7d367514745715fff332b652349f222/master
> $ git remote rm b7d367514745715fff332b652349f222
> $ git push

> $ git fetch --all --tags

# See also
* http://www.nomachetejuggling.com/2011/09/12/moving-one-git-repo-into-another-as-subdirectory/
