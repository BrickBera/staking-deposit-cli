FROM python:alpine3.14

WORKDIR /app

COPY requirements.txt setup.py ./

COPY staking_deposit ./staking_deposit

COPY --from=ghcr.io/foundry-rs/foundry /usr/local/bin/forge /usr/bin/forge 
COPY --from=ghcr.io/foundry-rs/foundry /usr/local/bin/cast /usr/bin/cast
COPY --from=ghcr.io/foundry-rs/foundry /usr/local/bin/anvil /usr/bin/anvil
COPY --from=ghcr.io/foundry-rs/foundry /usr/local/bin/chisel /usr/bin/chisel

RUN apk add --update gcc libc-dev linux-headers bash curl jq

RUN pip3 install -r requirements.txt

RUN python3 setup.py install

ARG cli_command

ENTRYPOINT [ "python3", "./staking_deposit/deposit.py" ]

CMD [ $cli_command ]
