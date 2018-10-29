# tweepy-api

## Setting up

```

Download code from repo: git clone https://github.com/jcastro39/DVA.git
Install python3 (preferably version 3.6.* since tweepy does not support 3.7.0)
If you currently have 3.7.0, run the following commands to switch versions with HomeBrew:
  1) brew unlink python
  2) brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
This will install version 3.6.5 and you can reverse the changes if needed as python 3.7.0 will still exist.

Check version after install: python3 --version

Use pip to install necessary packages:
  pip3 install tweepy
  pip3 install textblob
  pip3 install dataset
