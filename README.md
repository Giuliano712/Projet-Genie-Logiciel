# Gestionnaire de tâche

## Projet de Génie Logiciel

## Étudiants
-   **Erard** Julien ERAJ09050200
-   **Berlioz** Clément BERC13090100
-   **Seidlitz** Eloi SEIE25020100
-   **Hiblot-Mery** Clément HIBC24120200

## Séance 1 : 
# Personas 

<div style="width:80%; margin: auto;">
    <img src="media/Capture d'écran 2024-11-18 220317.png" alt="accueil" style="width:100%;">
</div>

<div style="width:80%; margin: auto;">
    <img src="media/Capture d'écran 2024-11-18 220336.png" alt="accueil" style="width:100%;">
</div>

<div style="width:80%; margin: auto;">
    <img src="media/Capture d'écran 2024-10-31 163123.png" alt="accueil" style="width:100%;">
</div>

# Scénarios

**Tom** : Le matin il arrive à 8h au bureau, il se connecte sur le gestionnaire de tâches, et consulte l’onglet messagerie instantanée pour voir s’il a reçu des messages. Après une pause à la machine à café, il se connecte ensuite au logiciel de gestion de tâches afin de voir quelles tâches ont été effectuée la veille pour prendre connaissance de l’avancement du projet. Il valide les tâches effectuées et assigne les nouvelles tâches à chaque employé. Après un problème sur une tâche il modifie sa dead line. 

**Patricia** : Patricia se lève et commence par consulter son planning détaillé de la journée réalisé par son chef de projet. Son objectif est de respecter au mieux ses délais tout en laissant du temps pour visiter des endroits locaux. Après une réunion avec son équipe à San Francisco, elle reçoit une notification qu’une tâche a été modifié, elle remarque que son collègue a laissé une remarque sur cette tâche. N’ayant pas compris sa remarque, Patricia envoie un message à ce collègue pour mieux comprendre. Dans l’après-midi, elle finit de programmer une interface utilisateur et elle indique la tâche qu’elle vient d’accomplir. 

**Yvan** : Yvan reçoit une notification comme quoi il y a une nouvelle version du chatbot et se connecte à la plateforme pour la tester. Il observe les bons côtés et les éléments à améliorer selon les réponses du chatbot. Il formule la réponse que devrait avoir le chatbot et le fait dans un document Excel. Lors de la réunion hebdomadaire avec le chef de projet et potentiellement des développeurs il explique et précise son besoin et sa vision en fonction de l’avancement du projet pour guider les décisions futures de l’équipe de développement.

## Séance 2 :
# Histoires Utilisateur

**Tom** :  
En tant que gestionnaire de projet, je dois avoir un outil permettant de créer des tâches et les assignés à un développeur et avoir la possibilité de consulter l’état de cette tâche. 
En tant que gestionnaire de projet, j’ai besoin d’un tableau de bord afin de voir quelles tâches ont été effectuées et prendre connaissance de l’avancement du projet. 
En tant que gestionnaire de projet, je souhaite avoir un outil de messagerie pour communiquer avec mes équipes, afin de leur faire parvenir des tâches spécifiques ou des changements dans leur code.  
En tant que gestionnaire de projet, je dois avoir un outil de calendrier afin de planifier l’avancement du projet et gérer les délais de livraison du produit.  

**Patricia** : 
En tant que développeuse, j’ai besoin de voir les tâches qui me sont attribuées, afin de savoir sur quoi je dois travailler chaque jour. 
En tant que développeuse, j’ai besoin d’un outil de communication avec mes collaborateurs, afin de discuter de sujets liés au projet. 
En tant que développeuse, j’ai besoin de recevoir des notifications en cas de changements sur mes tâches, afin d’être toujours au courant des dernière mises à jour du projet. 
En tant que développeuse, j’ai besoin de mettre des commentaires sur les tâches qui me sont attribuées, afin d’exprimer les difficultés que je rencontre ou de proposer à mes collaborateurs d’éventuels amendements sur ces tâches. 

 
**Yvan** : 
En tant que client, j’ai besoin d’un tableau de bord afin de voir l’avancement du projet en temps réel. 
En tant que client, j’ai besoin d’un outil de messagerie pour communiquer avec le chef de projet pour avoir des retours sur l’état de mon projet. 
En tant que client, j’ai besoin d’un outil de test pour pouvoir tester les différentes versions du projet 
En tant que client, je peux mettre des feedbacks sur les différentes versions du projet afin de mieux diriger les équipes vers le produit que je veux. 

# Liste de fonctionnalité
Client : C ; Développeur : D ; Chef de projet : CP ; 

1. Pouvoir se connecter aux différents types d’utilisateurs. (C, D, CP) 

2. Pouvoir visualiser les tâches du projet et leur état (en cours, terminé ou pas commencé). (C, D, CP) 

3. Pouvoir catégoriser les tâches en fonction de leur importance. (CP) 

4. Pouvoir mettre à jour l’état d’une tâche. (D, CP) 

5. Pouvoir ajouter de nouvelles tâches et les assigner à chaque équipe. (CP) 

6. Pouvoir modifier les deadlines des tâches. (CP) 

7. Pouvoir communiquer sur un espace messagerie. (C, D, CP) 

8. Pouvoir mettre des commentaires sur les tâches. (C, D, CP) 

9. Pouvoir accéder aux différentes versions du projet. (C, D, CP)  

# Prototype 

### Sur papier

<div style="width:80%; margin: auto;">
    <img src="media/DraftForFigma1.0.jpeg" alt="accueil" style="width:100%;">
</div>

<div style="width:80%; margin: auto;">
    <img src="media/DraftForFigma2.0.jpeg" alt="accueil" style="width:100%;">
</div>

### Figma

<div style="width:80%; margin: auto;">
    <img src="media/FigmaScreenshot.png" alt="accueil" style="width:100%;">
</div>

https://www.figma.com/design/a8tNdS0GlsUN2EUFGjYkza/Untitled?node-id=70-422&node-type=frame&t=quIiounqUOAMnQXf-0

# Fonctionnalités Nécessaires

### Réalisées

1. S'enregistrer (connexion)
2. Se connecter en tant que Chef de Projet (connexion)
3. Ajouter une nouvelle tâche (gestion des tâches)
4. Possibilité de voir si une tâche est : Faite, En cours, À faire (visualisation de l'avancement)

### En cours

### À faire

5. Se connecter en tant que Développeur (connexion)
6. Se connecter en tant que Client (connexion)
7. Visualiser de l'avancement en tant que Développeur (visualisation de l'avancement)
8. Visualiser de l'avancement en tant que Client (visualisation de l'avancement)
9. Modifier une tâche existante (gestion des tâches)
10. Modifier l'avancement d'une tâche par le Développeur ou le Chef de Projet (gestion des tâches)

# Tests


### Réalisées

1. L'utilisateur peux s'enregistrer, se connecter et accéder à la page de planning
2. Le mot de passe ne peux pas être "password"
3. Le mot de passe doit avoir au moins 8 caractères
4. Le mot de passe ne peux pas être constitué uniquement de chiffres

### En cours



### À faire



# Améliorations

### Réalisées



### En cours



### À faire

1. Adapter la visualisation actuelle de l'application à celle dans Figma
      - *Clément Hiblot-Mery*

# Fonctionnalitées Optionnelles Prioritaires


### À faire

1. Pouvoir mettre des commentaires sur les tâches
2. Service de messagerie entre utilisateurs

# Fonctionnalitées Optionnelles Non-Prioritaires


### À faire

1. Service de messagerie entre utilisateur et chatbot
2. Possibilité pour le Développeur de dépoyer du code pour l'utilisation du chatbot par le client
