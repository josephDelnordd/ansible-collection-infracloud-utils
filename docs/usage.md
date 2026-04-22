# Guide d'utilisation - infracloud.utils

## Installation

### Depuis Ansible Galaxy

```bash
ansible-galaxy collection install infracloud.utils
```

### Depuis GitHub

```bash
ansible-galaxy collection install git+https://github.com/VOTRE_USERNAME/ansible-collection-infracloud-utils.git
```

### Depuis un fichier tar.gz

```bash
ansible-galaxy collection install infracloud-utils-1.0.0.tar.gz
```

## Rôle : server_maintenance

### Variables disponibles

Variable | Défaut | Description |
-------------------|------------------|------------------|
ssh_banner_enabled	| true	| Active la bannière SSH |
ssh_banner_file	| /etc/ssh/banner	| Chemin du fichier bannière |
company_name	| InfraCloud	| Nom affiché dans la bannière |
company_environment	| Production	| Environnement affiché |

## Exemple

```yaml
- hosts: webservers
  become: yes
  roles:
    - role: infracloud.utils.server_maintenance
      vars:
        company_environment: "Staging"
```

## Module : check_disk

### Paramètres

Paramètre | Requis | Défaut | Description |
------------------- | ------------------ |------------------ | ------------------ |
path | oui | / | Partition à vérifier |
threshold | non | 80 | Seuil d'alerte (%) |

### Exemple

```yaml
- name: Vérifier l'espace disque
  infracloud.utils.check_disk:
    path: "/"
    threshold: 85
  register: result
```

