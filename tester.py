import subprocess
import csv

# Fonction pour exécuter plusieurs commandes successivement
def execute_commands(process, commands):
    final_stdout = ""
    final_stderr = ""

    for command in commands:
        # Exécuter une commande
        process.stdin.write(command + "\n")
        process.stdin.flush()  # Forcer l'écriture immédiate dans stdin

    # Attendre la sortie
    out, err = process.communicate()  # Exécution et capture des outputs
    final_stdout += out
    final_stderr += err

    return final_stdout, final_stderr


# Fonction testing pour plusieurs commandes successives
def testing(commands):
    # Séparer les commandes par saut de ligne
    commands = commands.strip().split("\n")

    # Lancer bash
    procbash = subprocess.Popen(["bash"],
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)

    # Lancer minishell
    procmini = subprocess.Popen(["bash"], #remplace par ./minishell
                                 stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 text=True)

    # Exécuter les commandes successivement dans bash et minishell
    outb, errb = execute_commands(procbash, commands)
    outm, errm = execute_commands(procmini, commands)

    # Comparer les sorties finales
    if outb == outm and errb == errm:
        print(f"✅ Commandes exécutées -> IDENTIQUES")
    elif outb == outm and errb != errm:
        print(f"❌ Commandes exécutées -> Codes d'erreur DIFFÉRENTS")
        print("---- Sortie Bash ----")
        print(f"stderr : {errb}")
        print("---- Sortie Minishell ----")
        print(f"stderr : {errm}")
    elif outb != outm and errb == errm:
        print(f"❌ Commandes exécutées -> Outputs DIFFÉRENTS")
        print("---- Sortie Bash ----")
        print(f"stdout : {outb}")
        print("---- Sortie Minishell ----")
        print(f"stdout : {outm}")
    else:
        print(f"❌ Commandes exécutées -> Codes d'erreur ET outputs DIFFÉRENTS")
        print("---- Sortie Bash ----")
        print(f"stdout : {outb}")
        print(f"stderr : {errb}")
        print("---- Sortie Minishell ----")
        print(f"stdout : {outm}")
        print(f"stderr : {errm}")

    # Fermer explicitement les processus après utilisation
    procbash.stdin.close()
    procbash.stdout.close()
    procbash.stderr.close()
    procmini.stdin.close()
    procmini.stdout.close()
    procmini.stderr.close()


# Lire les commandes depuis un fichier CSV
def read_commands_from_csv(filename):
    commands = []
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Sauter l'en-tête
            for row in reader:
                if len(row) >= 1:
                    command = row[0].strip()
                    category = row[1].strip() if len(row) > 1 else "Pas de catégorie"
                    commands.append((command, category))
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} est introuvable.")
    return commands


# Lancer les tests pour toutes les commandes
def run_tests_from_csv(filename):
    commands = read_commands_from_csv(filename)
    if not commands:
        print("Aucune commande à tester.")
        return

    for command, category in commands:
        print(f"\n--- Test de commandes : ---")
        print(f"Catégorie : {category}")
        print(f"Commandes :\n{command}")
        testing(command)


# Exemple d'appel avec un fichier "commands.csv"
run_tests_from_csv("commands.csv")


# Lire les commandes depuis un fichier CSV
def read_commands_from_csv(filename):
    commands = []
    try:
        with open(filename, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Sauter l'en-tête
            for row in reader:
                if len(row) >= 1:
                    command = row[0].strip()
                    category = row[1].strip() if len(row) > 1 else "Pas de catégorie"
                    commands.append((command, category))
    except FileNotFoundError:
        print(f"Erreur : le fichier {filename} est introuvable.")
    return commands


# Lancer les tests pour toutes les commandes
def run_tests_from_csv(filename):
    commands = read_commands_from_csv(filename)
    if not commands:
        print("Aucune commande à tester.")
        return

    for command, category in commands:
        print(f"\n--- Test de commandes : ---")
        print(f"Catégorie : {category}")
        print(f"Commandes :\n{command}")
        testing(command)


# Exemple d'appel avec un fichier "commands.csv"
run_tests_from_csv("commands.csv")
