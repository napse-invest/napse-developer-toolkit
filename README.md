<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/theme/assets/napse_invest_logo_white.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/theme/assets/napse_invest_logo_black.svg">
  <img alt="Napse's logo" src="" width=500>
</picture>
</div>

<br>
<p align="center">
  <a>
    <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/napse-investment/40fac957532fe3b731c99067467de842/raw/napse-developer-toolkit-coverage.json" alt="Coverage" />
  </a>
  <a>  
    <img src="https://img.shields.io/github/v/release/napse-invest/napse-developer-toolkit" alt="Release" />
  </a>
  <a href="https://twitter.com/NapseInvest">
    <img src="https://img.shields.io/twitter/follow/NapseInvest?style=flat&label=%40NapseInvest&logo=twitter&color=0bf&logoColor=fff" alt="Twitter" />
  </a>
  <a>  
    <img src="https://img.shields.io/discord/996867961157591081?style=flat&logo=discord&label=Napse%20Invest&link=https%3A%2F%2Fdiscord.gg%2FZkzc2V5KXB" alt="Discord" />
  </a>
</p>

<p align="center">
  <a href="#napse-developer-toolkit"><strong>Napse Developer Toolkit</strong></a> ·
  <a href="#setup-local-environment"><strong>Setup local environment</strong></a> .
  <a href="#run-project-with-docker"><strong>Docker</strong></a> .
  <a href="#useful-commands"><strong>Useful commands</strong></a>
</p>
<br/>

# Napse Developer Toolkit
All you need to push the customisation of your Napse services to the next level.


## Setup local environment

Local environment is use for your IDE, but it's not use to run napse-dtk. See [Run project with docker](#run-project-with-docker) for more information.

To setup your local environment:
```bash
make setup
```

## Run project with docker

- Start:
```bash
make up
```

## Useful commands

- Build:
```bash
make build
```

- Stop:
```bash
make down
```

- Run tests:
```bash
make test
```

- Run tests with coverage:
```bash
make coverage
# or
make coverage-open
```

- lightstream:
```bash
make litestream
```