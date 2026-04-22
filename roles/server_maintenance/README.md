# Role : server_maintenance

## Description

Role de maintenance serveur qui automatise :

- Installation des paquets de base
- Installation des outils de monitoring
- Configuration de la banniere SSH
- Activation des services systeme

## Variables

| Variable | Defaut | Description |
|---|---|---|
| ssh_banner_enabled | true | Active la banniere SSH |
| ssh_banner_file | /etc/ssh/banner | Chemin du fichier banniere |
| company_name | InfraCloud | Nom affiche dans la banniere |
| company_environment | Production | Environnement affiche |

## Systemes supportes

- Ubuntu 20.04 / 22.04 / 24.04
- Rocky Linux 8 / 9

## Exemple d'utilisation

```yaml
- hosts: all
  become: yes
  roles:
    - role: josephdelnordd.utils.server_maintenance
      vars:
        company_name: "MonEntreprise"
        company_environment: "Production"
```

## License

GPL-3.0-or-later
