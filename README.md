Project setup
=============


Bitcoin Full Node setup
++++++++++++++++++++++++

Install requirements::
  
    apt-get install g++ libtool make autoconf automake libdb++-dev libboost-all-dev

Addition installation steps::

    https://dev.to/ruanbekker/running-a-testnet-with-bitcoin-on-linux-4b0p


Install project requirements::

    git clone git@github.com:thenewboston-developers/Blockchain-Scanner.git
    cd Blockchain-Scanner
    poetry install
    poetry shell

Running example:: 

    export RPC_USER=bitcoin
    export RPC_PASSWORD='000000000000000000000000000000000000000000000000'
    
    python main --username ${RPC_USER} --password ${RPC_PASSWORD} \
    --amount 0.00101071 \
    --receiving-address tb1qgm2u43dsunmxhge63q7as84kh8cw98yyaltzyd \
    -tx a28008f442ca20f9eb9728fe10e8d603987456f2ea479a6cf1cb88ecaf476472


Ethereum Full Node setup
++++++++++++++++++++++++

Installation steps

1. Download latest binary version of Geth from https://github.com/ethereum/go-ethereum
2. Unpack archive.
3. Run Geth in light mode with RPC support::

    ./geth --syncmode "light" --http

Running example:: 

    python main -b ethereum -a 0.00101071 \
    -r 0xdac17f958d2ee523a2206206994597c13d831ec7 
    -t 0x4a5efe38157176293d5179f9940667d64a8d9126a0d4edf5d5aadc348cefee1b 
    --port 8545
