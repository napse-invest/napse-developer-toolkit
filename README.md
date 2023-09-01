<h1 align="center">
<img src="https://github.com/napse-invest/Napse/blob/main/desktop-app/renderer/public/images/napse_white.svg" width=500/>
</h1><br>

<p align="center">

  <a>
    <img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/napse-investment/40fac957532fe3b731c99067467de842/raw/napse-developer-toolkit-coverage.json" alt="Coverage" />
  </a>
  <a>  
    <img src="https://img.shields.io/github/v/release/napse-invest/django-napse" alt="Release" />
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
  <a href="#development environment"><strong>Development environment</strong></a>
</p>
<br/>

## Napse Developer Toolkit
All you need to push the customisation of your Napse services to the next level.

## Development environment

### Setup local environment

Local environment is use for your IDE, but it's not use to run napse-dtk. See [Run project with docker](#run-project-with-docker) for more information.

Run the setup script to fully setup your local environment:
- Unix \
```source setup-unix.sh```

- Windows (PowerShell terminal as administrator)\
```.\setup-windows.ps1```

### Run project with docker

- Start docker in development environment \
    ```docker-compose -f ./backend/docker/development.yml up --build -d```

- Start docker in development as production environment \
    ```docker-compose -f ./backend/docker/dev_as_prod.yml up --build -d```


## Useful commands

- Start docker \
    ```docker-compose -f ./backend/docker/<yml file> up --build -d```

- Stop docker \
    ```docker-compose -f ./backend/docker/<yml file> down```

-  Enter in the django container \
    ```docker exec -it napse_dtk_dev_django /bin/bash```
