# my_history
- parquet 파일의 정보를 cli 기반으로 조회

### 사용법
```
$ my-history -s ls
ls 사용 횟수는 1234회 입니다.

$ my-history -t 10 -d 2024-07-17
  cmd  cnt
pyenv 4256
   cd 3472
  git 3396
mkdir 1932
  pip 1592
  cat 1368
   vi 1356
 sudo 1320
  pdm 1220
   rm 1104
```

### Dev env setting
```
$ git clone <URL>
$ cd <Project_Name>
$ pyenv virtual lenv 3.11.9 empty
$ pyenv global empty
$ rm -rf .venv
$ pdm venv create
$ source .venv/bin/activate
$ pdm install
$ pdm list
$ pytest 

#option 

git install 말고 수동으로 했을 때
$ pdm init
$ pdm venv create
$ source .venv/bin/activate
$ pdm add -dG test pytest pytest-cov
```

### Deployment
```
# dev branch
$ pip install git+https://github.com/oddsummer56/my_history.git@0.2.0/args

# main
$ pip install git+ https://github.com/oddsummer56/my_history.git
```

### reference
- https://pdm-project.org/en/latest/usage/dependency/#add-development-only-dependencies

