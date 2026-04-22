# InfraCloud Utils Collection

## Description

Collection Ansible développée par l'équipe DevOps d'InfraCloud pour automatiser les tâches récurrentes de maintenance serveur.

## Contenu

### Rôles

- **server_maintenance** : Installation des paquets de base, configuration de la bannière SSH, déploiement d'outils de monitoring.

### Modules

- **check_disk** : Module custom qui vérifie l'espace disque disponible sur une partition et retourne un avertissement si le seuil est dépassé.

## Installation

```bash
ansible-galaxy collection install infracloud.utils
```
Ou depuis GitHub :

```bash
ansible-galaxy collection install git+https://github.com/VOTRE_USERNAME/ansible-collection-infracloud-utils.git
```

## Utilisation

```yaml
- hosts: all
  collections:
    - infracloud.utils
  roles:
    - server_maintenance
```

## Systèmes supportés

- Ubuntu 20.04 / 22.04 / 24.04
- Rocky Linux 8 / 9

## Licence

GPL-3.0-or-later