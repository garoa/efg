#!/bin/bash

# Verifique se o Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "Python3 não foi encontrado. Por favor, instale-o."
    exit
fi

# Execute doctest no arquivo README
python3 -m doctest README.md

# Verifique se o doctest foi executado com sucesso
if [ $? -eq 0 ]
then
    echo "OK"
fi
