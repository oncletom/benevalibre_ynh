# _Bénévalibre_ pour YunoHost

[![Niveau d'intégration](https://dash.yunohost.org/integration/benevalibre.svg)](https://dash.yunohost.org/appci/app/benevalibre) ![](https://ci-apps.yunohost.org/ci/badges/benevalibre.status.svg) ![](https://ci-apps.yunohost.org/ci/badges/benevalibre.maintain.svg)
[![Installer benevalibre avec YunoHost](https://install-app.yunohost.org/install-with-yunohost.svg)](https://install-app.yunohost.org/?app=benevalibre)

*[Read this readme in english.](./README.md)*

> *Ce package vous permet d'installer [Bénévalibre] rapidement et simplement sur un serveur YunoHost.
Si vous n'avez pas YunoHost, consultez [le guide](https://yunohost.org/#/install) pour apprendre comment l'installer.*

## Vue d'ensemble
Description rapide de cette application.

**Version incluse :** 1.1.0

## Captures d'écran

![](Lien vers une capture d'écran de cette application.)

## Démo

* [Démo officielle][Bénévalibre-démo]

## Configuration

Comment configurer cette application : via le panneau d'administration, un fichier brut en SSH ou tout autre moyen.

## Documentation

 * [Documentation officielle][Bénévalibre-doc]

## Caractéristiques spécifiques YunoHost

#### Support multi-utilisateur

⚠️ L'authentification via le portail SSO est en cours de développement.

#### Architectures supportées

* x86-64 - [![Build Status](https://ci-apps.yunohost.org/ci/logs/benevalibre%20%28Apps%29.svg)](https://ci-apps.yunohost.org/ci/apps/benevalibre/)
* ARMv8-A - [![Build Status](https://ci-apps-arm.yunohost.org/ci/logs/benevalibre%20%28Apps%29.svg)](https://ci-apps-arm.yunohost.org/ci/apps/benevalibre/)

## Limitations

* Limitations connues.

## Informations additionnelles

* Autres informations que vous souhaitez ajouter sur cette application.

**Plus d'informations sur la page de documentation :**
https://yunohost.org/packaging_apps

## Liens

 * Signaler un bug : https://github.com/YunoHost-Apps/benevalibre_ynh/issues
 * Site de l'application : Lien vers le site officiel de cette application.
 * Dépôt de l'application principale : Lien vers le dépôt officiel de l'application principale.
 * Site web YunoHost : https://yunohost.org/

---

## Informations pour les développeurs

**Seulement si vous voulez utiliser une branche de test pour le codage, au lieu de fusionner directement dans la banche principale.**
Merci de faire vos pull request sur la [branche testing](https://github.com/YunoHost-Apps/benevalibre_ynh/tree/testing).

Pour essayer la branche testing, procédez comme suit.
```
sudo yunohost app install https://github.com/YunoHost-Apps/benevalibre_ynh/tree/testing --debug
ou
sudo yunohost app upgrade benevalibre -u https://github.com/YunoHost-Apps/benevalibre_ynh/tree/testing --debug
```

[Bénévalibre]: https://benevalibre.org/
[Bénévalibre-démo]: https://app.benevalibre.org/
[Bénévalibre-doc]: https://app.benevalibre.org/docs/
