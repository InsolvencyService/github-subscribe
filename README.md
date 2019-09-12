# github-subscribe

Automate subscription of slack to GitHub repositories utilising [GitHub + Slack Integration](https://github.com/integrations/slack) App.

## Getting Started


### Prerequisites

* Python 2.x/3.x - tested against 2.7.12/3.6.9
* PIP
* A repository list - see contrib/sample-repolist.txt

### Installing

There is no installer but some pip modules are required
```
pip install -r requirements.txt
```

Replace your-slack-token with a legacy slack token in github-subscribe.py
```
slack = Slacker('your-slack-token')
```

Replace GithubOrganisation with the one it should work against
```
ftext = "GithubOrganisation/" + text
```

Copy sample-repolist.txt from contrib/ and update with a repo list
and run
```
python github-subscribe.py
```

## Built With

* [Slacker](https://github.com/os/slacker) - Full-featured Python interface for the Slack API

## Contributing

This code is not officially maintained and PRs are not likely to be actioned. Forks are encouraged.

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details
