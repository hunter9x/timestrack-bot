# timestrack-bot

Time tracking bot for Slack

## day0

* Try with [this sample](https://github.com/slackapi/python-message-menu-example/blob/master/example.py)

### Type of tokens

* [ref](https://api.slack.com/docs/token-types)

#### Bot user tokens

* begin with `xoxb-`

#### User tokens

* begin with `xoxp`

### os.environ

* [doc](https://docs.python.jp/3/library/os.html#os.environ)
* 環境変数を定義できるマップ型のオブジェクト
* basic usage:
* export the environment variable on shell

```shell
root $ export $SLACK='example'
```

* in py file just use `os.environ.get()`

```python
os.environ.get('SLACK')
```

### Readed ref

* [Getting Started With the Slack API Using Python and Flask](https://realpython.com/getting-started-with-the-slack-api-using-python-and-flask/)
