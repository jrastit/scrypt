#!/bin/bash

# Installer pour l'environnement Starkli

echo "Installation de Starkliup..."
curl https://get.starkli.sh | sh

. ~/.starkli/env

# Installation de Starkli
echo "Installation de Starkli..."
starkliup


# Vérification de l'installation de Starkli
echo "Vérification de l'installation de Starkli..."
bash -c starkli --version