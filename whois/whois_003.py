#!/usr/bin/python

import whois

target ="google.com"


def func_whois(_domain):
    querywhois = whois.query(_domain)
    print("[+] - Nome do dominio: ", querywhois.name)
    print("[+] - Data de criacao: ", querywhois.creation_date)
    print("[+] - Data de expiracao: ", querywhois.expiration_date)
    print("[+] - Data de ultima atualizacao: ", querywhois.last_updated)
    print("[+] - Servidor whois registrado: ", querywhois.registrar)


    for _domain in querywhois.name_servers:
         print("[+] - Servidor de nomes: ", _domain)

func_whois(target)

