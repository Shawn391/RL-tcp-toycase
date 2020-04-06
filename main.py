''' Voglio un main che:
1. chiami ciascuno degli algoritmi
2. passandogli i parametri (episodi, epsilon, lambda, ecc)
3. che verifichi che sia arrivato alla policy ottimale
4. che calcoli il reward di quella policy
5. che salvi il numero di episodi
6. che quantifichi il quanto siamo vicini alla policy ottimale (come faccio?)
7. che plotti con questi valori il numero di episodi per arrivare alla policy ottimale
'''
from qlearning_simplified_class import QlearningSimplified
from sarsa_simplified_class import SarsaSimplified
from sarsa_lambda_simplified_class import SarsaLambdaSimplified
import matplotlib.pyplot as plt

num_episodes = 200
factor = 10
x = []
y_sarsa_rewards = []
y_sarsa_lambda_rewards = []
y_qlearning_rewards = []

dis = True

print("SARSA")
n = 0
while n < num_episodes:
    x.append(n)
    optimalPolicy, obtainedReward = SarsaSimplified(total_episodes=n, disable_graphs=dis).run()
    if dis == False:
        if optimalPolicy:
            print("[SARSA] Optimal policy was found with reward", obtainedReward)
        else:
            print("[SARSA] No optimal policy reached with reward", obtainedReward)
    y_sarsa_rewards.append(obtainedReward)
    n += factor

print("SARSA(lambda)")
n = 0
while n < num_episodes:
    optimalPolicy, obtainedReward = SarsaLambdaSimplified(total_episodes=n,lam=0.5, disable_graphs=dis).run()
    if dis == False:
        if optimalPolicy:
            print("[SARSA(lambda)] Optimal policy was found with reward", obtainedReward)
        else:
            print("[SARSA(lambda)] No optimal policy reached with reward", obtainedReward)
    y_sarsa_lambda_rewards.append(obtainedReward)
    n += factor

print("Q-learning")
n = 0
while n < num_episodes:
    optimalPolicy, obtainedReward = QlearningSimplified(total_episodes=n, disable_graphs=dis).run()
    if dis == False:
        if optimalPolicy:
            print("[Q-learning] Optimal policy was found with reward", obtainedReward)
        else:
            print("[Q-learning] No optimal policy reached with reward", obtainedReward)
    y_qlearning_rewards.append(obtainedReward)
    n += factor

print("End of episodes, showing graph...")
plt.plot(x, y_sarsa_rewards, label="Sarsa")
plt.plot(x, y_sarsa_lambda_rewards, label="Sarsa Lambda")
plt.plot(x, y_qlearning_rewards, label="Q-Learning")
plt.xlabel('Episodes')
plt.ylabel('Final policy reward')
plt.title('Simplified: Final policy over number of episodes chosen.')
plt.legend()
plt.show()
